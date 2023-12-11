import numpy as np

with open("day10.in") as f:
    fuck = f.readlines()

grid = []
for line in fuck:
    grid.append(line.strip("\n"))

for line in grid:
    print(line)


def part1():
    start = find_start()
    path1 = []
    path2 = []
    dir = 0  # N E S W
    if path1 == []:
        if grid[start[0] - 1][start[1]] in "|7F":
            path1 = [start[0] - 1, start[1]]
        dir += 1
    if path1 == []:
        if grid[start[0]][start[1] + 1] in "-7J":
            path1 = [start[0], start[1] + 1]
        dir += 1
    if path1 == []:
        if grid[start[0] + 1][start[1]] in "|LJ":
            path1 = [start[0] + 1, start[1]]
        dir += 1
    if path1 == []:
        if grid[start[0]][start[1] - 1] in "-LF":
            path1 = [start[0], start[1] - 1]

    if dir == 0:
        if grid[start[0] - 1][start[1]] in "|7F":
            path2 = [start[0] - 1, start[1]]
        dir += 1
    if dir == 1:
        if grid[start[0]][start[1] + 1] in "-7J":
            path2 = [start[0], start[1] + 1]
        dir += 1
    if dir == 2:
        if grid[start[0] + 1][start[1]] in "|LJ":
            path2 = [start[0] + 1, start[1]]
        dir += 1
    if dir == 3:
        if grid[start[0]][start[1] - 1] in "-LF":
            path2 = [start[0], start[1] - 1]

    print(start, path1, path2)
    # print(grid[start[0]][start[1]])
    # print(grid[path1[0]][path1[1]])
    # print(grid[path2[0]][path2[1]])

    global seen
    seen = []
    seen.append(path1)
    seen.append(path2)
    prev1 = start
    prev2 = start
    count = 1
    while path1 != path2:
        # print(count)
        prev1, path1 = traverse(prev1, path1)
        prev2, path2 = traverse(prev2, path2)
        seen.append(path1)
        seen.append(path2)
        count += 1
    return count


def traverse(prev, cur):
    symbol = grid[cur[0]][cur[1]]
    # print(symbol)
    x_diff = cur[1] - prev[1]  # positive, came from left, negative, came from right
    y_diff = cur[0] - prev[0]  # positive, came from up, negative, came from down

    if x_diff == 1:
        if symbol == "-":
            return cur, [cur[0], cur[1] + 1]
        if symbol == "7":
            return cur, [cur[0] + 1, cur[1]]
        if symbol == "J":
            return cur, [cur[0] - 1, cur[1]]

    if x_diff == -1:
        if symbol == "-":
            return cur, [cur[0], cur[1] - 1]
        if symbol == "F":
            return cur, [cur[0] + 1, cur[1]]
        if symbol == "L":
            return cur, [cur[0] - 1, cur[1]]

    if y_diff == 1:
        if symbol == "|":
            return cur, [cur[0] + 1, cur[1]]
        if symbol == "L":
            return cur, [cur[0], cur[1] + 1]
        if symbol == "J":
            return cur, [cur[0], cur[1] - 1]

    if y_diff == -1:
        if symbol == "|":
            return cur, [cur[0] - 1, cur[1]]
        if symbol == "F":
            return cur, [cur[0], cur[1] + 1]
        if symbol == "7":
            return cur, [cur[0], cur[1] - 1]
    print(cur)
    print(x_diff, y_diff, symbol)


def find_start():
    for row, line in enumerate(grid):
        if "S" in line:
            for col, char in enumerate(line):
                if char == "S":
                    return [row, col]


print(part1())
