import numpy as np

with open("2023/day23.in") as f:
    fuck = f.readlines()

sym_grid = []
for line in fuck:
    sym_grid.append(list(line.strip("\n")))

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

cardinals = [UP, LEFT, DOWN, RIGHT]


def main():
    intersections = get_intersections(sym_grid)
    nodes = [Node((-1, 1)), Node((len(sym_grid), len(sym_grid[0]) - 2))]
    sym_grid[0][1] = "v"
    sym_grid[len(sym_grid) - 1][len(sym_grid[0]) - 2] = "v"
    for intersection in intersections:
        nodes.append(Node(intersection))

    for node in nodes:
        node.find_next_nodes(nodes)

    graph = Graph(nodes)
    print(graph, end="\n\n")
    # part1(graph)
    part2(graph)


def part1(graph):
    print(graph.dfs())


def part2(graph):
    graph = graph.undirected()
    print(graph, end="\n\n")

    # for node in graph.nodes:
    #     print(f"{node}: {node.edges}")
    print(graph.exhaustive_dfs() - 2)

    # graph = graph.inverse()
    # print(graph, end="\n\n")
    # max_length = graph.max_path()
    # print(max_length)


class Graph:
    def __init__(self, nodes, start=None, end=None):
        self.nodes = nodes
        self.edges = []
        self.create_edges()
        self.start = start
        self.end = end
        if self.start == None and self.end == None:
            self.find_endpoints()

    def inverse(self):
        new_nodes = {}
        for node in self.nodes:
            new_nodes[node.pos] = Node(node.pos)

        for edge in self.edges:
            new_nodes[edge.dest.pos].edges.append(
                Edge(new_nodes[edge.dest.pos], new_nodes[edge.src.pos], edge.weight)
            )

        return Graph(list(new_nodes.values()))

    def undirected(self):
        new_nodes = {}
        for node in self.nodes:
            new_nodes[node.pos] = Node(node.pos)

        for edge in self.edges:
            new_nodes[edge.dest.pos].edges.append(
                Edge(new_nodes[edge.dest.pos], new_nodes[edge.src.pos], edge.weight)
            )
            new_nodes[edge.src.pos].edges.append(
                Edge(new_nodes[edge.src.pos], new_nodes[edge.dest.pos], edge.weight)
            )

        return Graph(
            list(new_nodes.values()), new_nodes[self.start.pos], new_nodes[self.end.pos]
        )

    def max_path(self, start=None, path_length=0):
        if start == None:
            start = self.start
        current_node = start
        path = str(current_node)

        while current_node.edges != []:
            max_edge = current_node.edges[0]
            for edge in current_node.edges:
                if edge.weight > max_edge.weight:
                    max_edge = edge
            path += f" --{max_edge.weight}-> {max_edge.dest}"
            path_length += max_edge.weight
            current_node = max_edge.dest

        print(path)

        return path_length

    def dfs(self, end=None, start=None, path_length=0):
        if start == None:
            start = self.start
        if end == None:
            end = self.end
        stack = [(start, path_length)]
        paths = {}
        parents = {}
        for node in self.nodes:
            paths[node.pos] = 0

        while len(stack) != 0:
            current_node, current_length = stack.pop()
            paths[current_node.pos] = current_length

            for edge in current_node.edges:
                if paths[edge.dest.pos] < current_length + edge.weight:
                    stack.append((edge.dest, current_length + edge.weight))
                    parents[edge.dest.pos] = edge

        current_edge = parents[end.pos]
        path = str(current_edge.dest)
        while current_edge.src.pos in parents:
            path = f"{current_edge.src} --{current_edge.weight}-> " + path
            current_edge = parents[current_edge.src.pos]
        path = f"{current_edge.src} --{current_edge.weight}-> " + path

        print(path)

        return paths[end.pos] - 2

    def exhaustive_dfs(self, current_node=None, visited=[]):
        # print(current_node)
        # print(visited)
        if current_node == self.end:
            return 0
        if current_node == None:
            current_node = self.start

        dead_end = True
        max_length = -99999
        visited.append(current_node)
        for edge in current_node.edges:
            if edge.dest not in visited:
                # print(f"{current_node}: visiting: {edge.dest}\n")
                dead_end = False
                result = self.exhaustive_dfs(edge.dest, visited) + edge.weight
                if result > max_length:
                    max_length = result

        # print(current_node)
        visited.remove(current_node)
        if dead_end:
            return -99999

        return max_length

    def find_endpoints(self):
        node_pos = []
        for node in self.nodes:
            node_pos.append(node.pos)

        for edge in self.edges:
            if edge.dest.pos in node_pos:
                node_pos.remove(edge.dest.pos)

        for node in self.nodes:
            if node.pos == node_pos[0]:
                self.start = node
            if node.edges == []:
                self.end = node

    def create_edges(self):
        for node in self.nodes:
            self.edges += node.edges

    def __str__(self):
        out = str(self.nodes) + "\n"
        for edge in self.edges:
            out += str(edge) + "\n"
        return out


class Node:
    def __init__(self, pos):
        self.pos = pos
        self.edges = []

    def get_out_dirs(self):
        dirs = []
        if get_symbol(pos_add(self.pos, UP)) == "^":
            dirs.append(UP)

        if get_symbol(pos_add(self.pos, DOWN)) == "v":
            dirs.append(DOWN)

        if get_symbol(pos_add(self.pos, LEFT)) == "<":
            dirs.append(LEFT)

        if get_symbol(pos_add(self.pos, RIGHT)) == ">":
            dirs.append(RIGHT)

        return dirs

    def find_next_nodes(self, nodes):
        dirs = self.get_out_dirs()
        for dir in dirs:
            path_length = 3
            loc = pos_add(pos_add(self.pos, dir), dir)
            # print("aaaa" + loc)
            last_dir = dir
            while get_symbol(loc) == ".":
                path_length += 1
                for card in cardinals:
                    if (
                        card != inv_dir(last_dir)
                        and get_symbol(pos_add(loc, card)) != "#"
                    ):
                        last_dir = card
                        loc = pos_add(loc, card)
                        break
            next_node_pos = pos_add(loc, last_dir)
            for node in nodes:
                if node.pos == next_node_pos:
                    self.edges.append(Edge(self, node, path_length))
                    break

    def __str__(self):
        return str(self.pos)

    def __repr__(self):
        return self.__str__()


class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __str__(self):
        return f"{self.src} --{self.weight}-> {self.dest}"

    def __repr__(self):
        return self.__str__()


def pos_add(pos1, pos2):
    return tuple(map(lambda i, j: i + j, pos1, pos2))


def inv_dir(dir):
    return (dir[0] * -1, dir[1] * -1)


def get_symbol(pos):
    if is_inbounds(sym_grid, pos):
        return sym_grid[pos[0]][pos[1]]
    return "#"


def old_part1(sym_grid):
    start = (0, 1)
    end = (len(sym_grid) - 1, len(sym_grid[0]) - 2)
    print(start)
    grid = bfs(sym_grid, start)
    print_grid(grid)
    # res = find_even_under_val(grid, 64)
    print(grid[end[0]][end[1]])


def bfs(sym_grid, start):
    grid = [[-1] * len(sym_grid[0]) for _ in range(len(sym_grid))]
    queue = [(start, None)]
    grid[start[0]][start[1]] = 0
    while len(queue) > 0:
        current, parent = queue.pop(0)

        # print(current)

        # print_grid(grid)

        weight = get_cell_val(grid, current) + 1

        if (
            is_inbounds(sym_grid, (current[0] - 1, current[1]))
            and get_cell_val(grid, current, -1, 0) < weight
            and sym_grid[current[0] - 1][current[1]] != "v"
            and parent != (current[0] - 1, current[1])
        ):
            queue.append(((current[0] - 1, current[1]), current))
            grid[current[0] - 1][current[1]] = weight
        if (
            is_inbounds(sym_grid, (current[0], current[1] - 1))
            and get_cell_val(grid, current, 0, -1) < weight
            and sym_grid[current[0]][current[1] - 1] != ">"
            and parent != (current[0], current[1] - 1)
        ):
            queue.append(((current[0], current[1] - 1), current))
            grid[current[0]][current[1] - 1] = weight
        if (
            is_inbounds(sym_grid, (current[0] + 1, current[1]))
            and get_cell_val(grid, current, 1, 0) < weight
            and sym_grid[current[0] + 1][current[1]] != "^"
            and parent != (current[0] + 1, current[1])
        ):
            queue.append(((current[0] + 1, current[1]), current))
            grid[current[0] + 1][current[1]] = weight
        if (
            is_inbounds(sym_grid, (current[0], current[1] + 1))
            and get_cell_val(grid, current, 0, 1) < weight
            and sym_grid[current[0]][current[1] + 1] != "<"
            and parent != (current[0], current[1] + 1)
        ):
            queue.append(((current[0], current[1] + 1), current))
            grid[current[0]][current[1] + 1] = weight

    return grid


def is_intersection(grid, coord):
    count = 0
    if grid[coord[0]][coord[1]] == "#":
        return False

    if grid[coord[0] - 1][coord[1]] in ["v", "^", "<", ">"]:
        count += 1

    if grid[coord[0] + 1][coord[1]] in ["v", "^", "<", ">"]:
        count += 1

    if grid[coord[0]][coord[1] - 1] in ["v", "^", "<", ">"]:
        count += 1

    if grid[coord[0]][coord[1] + 1] in ["v", "^", "<", ">"]:
        count += 1

    return count >= 3


def get_cell_val(grid, coord, yoff=0, xoff=0):
    return grid[coord[0] + yoff][coord[1] + xoff]


def is_inbounds(grid, pos):
    return (
        pos[0] >= 0
        and pos[1] >= 0
        and pos[0] < len(grid[0])
        and pos[1] < len(grid)
        and grid[pos[0]][pos[1]] != "#"
    )


def print_grid(grid):
    for row in grid:
        for char in row:
            if char == -1:
                print(f"   ", end=" ")
            else:
                print(f"{char:3}", end=" ")
        print()


def get_intersections(grid):
    intersections = []
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if is_intersection(grid, (i, j)):
                intersections.append((i, j))
    return intersections


main()
