import numpy as np

with open("day16.in") as f:
    fuck = f.readlines()

inp = []
for line in fuck:
    inp.append(line.strip("\n"))
    
# print(inp)
    
grid = []
for line in inp:
    grid.append([])
    for char in line:
        grid[-1].append(char)
        
# print(grid)
    

def part1():
    heads = []
    seen = []
    heads.append((0, 0, '>')) # y, x, dir
    grid[0][0] = '>'
    while(len(heads) != 0):
        traverse(heads, seen)
        
    print_grid()
        # input()
        # print(grid)
        # print(len(seen))
        
    return len(seen)
        
    
def print_grid():
    for line in grid:
        for char in line:
            print(char, end='')
        print()
    print()


def traverse(heads, seen):
    y, x, dir = heads[0]
    height = len(grid)
    width = len(grid[0])
    if y < 0 or y >= height or x < 0 or x >= width:
        heads.pop(0)
        return
    if (y, x) not in seen:
        seen.append((y, x))
        
    if dir == '>':
        if x + 1 >= width:
            heads.pop(0)
            return
        next = grid[y][x+1]
        
        if next == '.':
            heads[0] = (y, x+1, dir)
            grid[y][x+1] = dir
            return
        
        if next == '-':
            heads[0] = (y, x+1, dir)
            return
            
        if next == '|':
            heads[0] = (y, x+1, '^')
            heads.insert(0, (y, x+1, 'v'))
            return
            
        if next == '/':
            heads[0] = (y, x+1, '^')
            return
            
        if next =='\\':
            heads[0] = (y, x+1, 'v')
            return
            
        if next == '^' or next == 'v' or next == '2' or next == '<':
            heads[0] = (y, x+1, dir)
            grid[y][x+1] = '2'
            return
        
        heads.pop(0)
            
    if dir == '<':
        if x - 1 < 0:
            heads.pop(0)
            return
        next = grid[y][x-1]
        
        if next == '.':
            heads[0] = (y, x-1, dir)
            grid[y][x-1] = dir
            return
        
        if next == '-':
            heads[0] = (y, x-1, dir)
            return
            
        if next == '|':
            heads[0] = (y, x-1, '^')
            heads.insert(0, (y, x-1, 'v'))
            return
            
        if next == '/':
            heads[0] = (y, x-1, 'v')
            return
            
        if next =='\\':
            heads[0] = (y, x-1, '^')
            return
            
        if next == '^' or next == 'v' or next == '2' or next == '>':
            heads[0] = (y, x-1, dir)
            grid[y][x-1] = '2'
            return
        
        heads.pop(0)
        
    if dir == '^':
        if y - 1 < 0:
            heads.pop(0)
            return
        next = grid[y-1][x]
        
        if next == '.':
            heads[0] = (y-1, x, dir)
            grid[y-1][x] = dir
            return
        
        if next == '|':
            heads[0] = (y-1, x, dir)
            return
            
        if next == '-':
            heads[0] = (y-1, x, '<')
            heads.insert(0, (y-1, x, '>'))
            return
            
        if next == '/':
            heads[0] = (y-1, x, '>')
            return
            
        if next =='\\':
            heads[0] = (y-1, x, '<')
            return
            
        if next == '<' or next == '>' or next == '2' or next == 'v':
            heads[0] = (y-1, x, dir)
            grid[y-1][x] = '2'
            return
        
        heads.pop(0)
        
        
        
    if dir == 'v':
        if y + 1 >= height:
            heads.pop(0)
            return
        next = grid[y+1][x]
        
        if next == '.':
            heads[0] = (y+1, x, dir)
            grid[y+1][x] = dir
            return
        
        if next == '|':
            heads[0] = (y+1, x, dir)
            return
            
        if next == '-':
            heads[0] = (y+1, x, '<')
            heads.insert(0, (y+1, x, '>'))
            return
            
        if next == '/':
            heads[0] = (y+1, x, '<')
            return
            
        if next =='\\':
            heads[0] = (y+1, x, '>')
            return
            
        if next == '<' or next == '>' or next == '2' or next == '^':
            heads[0] = (y+1, x, dir)
            grid[y+1][x] = '2'
            return
        
        heads.pop(0)
        
        
print(part1())