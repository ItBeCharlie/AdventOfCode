import numpy as np

with open("day21.in") as f:
    fuck = f.readlines()

grid = []
for line in fuck:
    grid.append(line.strip("\n"))


def main(sym_grid):
    start = find_start(sym_grid)
    print(start)
    grid = bfs(sym_grid, start)
    print_grid(grid)
    res = find_even_under_val(grid, 64)
    print(res)


def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                return (i, j)


def bfs(sym_grid, start):
    grid = [[-1] * len(sym_grid[0]) for _ in range(len(sym_grid))]
    stack = [start]
    grid[start[0]][start[1]] = 0
    while len(stack) > 0:
        current = stack.pop(0)

        weight = grid[current[0]][current[1]] + 1
        if (
            is_inbounds(sym_grid, (current[0] - 1, current[1]))
            and grid[current[0] - 1][current[1]] == -1
        ):
            stack.append((current[0] - 1, current[1]))
            grid[current[0] - 1][current[1]] = weight
        if (
            is_inbounds(sym_grid, (current[0], current[1] - 1))
            and grid[current[0]][current[1] - 1] == -1
        ):
            stack.append((current[0], current[1] - 1))
            grid[current[0]][current[1] - 1] = weight
        if (
            is_inbounds(sym_grid, (current[0] + 1, current[1]))
            and grid[current[0] + 1][current[1]] == -1
        ):
            stack.append((current[0] + 1, current[1]))
            grid[current[0] + 1][current[1]] = weight
        if (
            is_inbounds(sym_grid, (current[0], current[1] + 1))
            and grid[current[0]][current[1] + 1] == -1
        ):
            stack.append((current[0], current[1] + 1))
            grid[current[0]][current[1] + 1] = weight

    return grid


def is_inbounds(grid, pos):
    return (
        pos[0] >= 0
        and pos[1] >= 0
        and pos[0] < len(grid[0])
        and pos[1] < len(grid)
        and grid[pos[0]][pos[1]] == "."
    )


def print_grid(grid):
    for row in grid:
        for char in row:
            if char == -1:
                print(f"   ", end=" ")
            else:
                print(f"{char:3}", end=" ")
        print()


def find_even_under_val(grid, val):
    count = 0
    for row in grid:
        for num in row:
            if num % 2 == 0 and num <= val:
                count += 1
    return count


main(grid)
