import numpy as np

with open("day11.in") as f:
    fuck = f.readlines()

grid = []
for line in fuck:
    grid.append(line.strip("\n"))   
    

def print_grid():
    for line in grid:
        print(line)
    

def expand_universe():
    i = 0
    all_dots = '.' * len(grid[0])
    print_grid()
    while i < len(grid):
        if grid[i] == all_dots:
            grid.insert(i, all_dots)
            i += 1
        i += 1
    print()
    print_grid()
    
    i = 0
    while i < len(grid[0]):
        good = True
        for j in range(len(grid)):
            if grid[j][i] != '.':
                good = False
                break
        if good:
            for j in range(len(grid)):
              grid[j] = grid[j][:i] + '.' + grid[j][i:]  
            i += 1
        i += 1
    
    print()
    print_grid()
    
    
def find_galaxies(row_offset, col_offset, gap = 2):
    galaxies = []
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '#':
                galaxies.append((y + (gap-1)*row_offset[y], x + (gap-1)*col_offset[x]))
    return galaxies


def distance_between_galaxies(galaxies):
    count = 0
    for index, galaxy in enumerate(galaxies):
        for i in range(index + 1, len(galaxies)):
            count += abs(galaxy[1] - galaxies[i][1]) + abs(galaxy[0] - galaxies[i][0])
            
    return count


def find_row_col_offset():
    empty_rows = []
    empty_cols = []
    row_count = 0
    col_count = 0
    i = 0
    all_dots = '.' * len(grid[0])
    while i < len(grid):
        if grid[i] == all_dots:
            row_count += 1
        empty_rows.append(row_count)
        i += 1
    
    i = 0
    while i < len(grid[0]):
        good = True
        for j in range(len(grid)):
            if grid[j][i] != '.':
                good = False
                break
        if good:
            col_count += 1
        empty_cols.append(col_count)
        i += 1

    return empty_rows, empty_cols

def part1():
    # expand_universe()
    row_offset, col_offset = find_row_col_offset()
    galaxies = find_galaxies(row_offset, col_offset, 2)
    # print(galaxies)
    return distance_between_galaxies(galaxies)
    

def part2():
    row_offset, col_offset = find_row_col_offset()
    # print(row_offset)
    # print(col_offset)
    galaxies = find_galaxies(row_offset, col_offset, 1000000)
    return distance_between_galaxies(galaxies)
    




# print(part1())
print(part2())