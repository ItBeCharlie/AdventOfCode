import numpy as np
import math

with open('day8.in') as f:
    fuck = f.readlines()

inp = []
for line in fuck:
    inp.append(line.strip('\n'))
    
sequence = inp[0]
left = {}
right = {}
starting = []

def parse(lines):
    global left, right, starting
    lines = lines[2:]
    for line in lines:
        head = line[0:3]
        if head[-1] == 'A':
            starting.append(head)
        left[head] = line[7:10]
        right[head] = line[12:15]
    
    # print(left)
    # print(right)
        
    

def part1(cur):
    steps = 0
    while cur[-1] != 'Z':
        if sequence[steps % len(sequence)] == 'L':
            cur = left[cur]
        else:
            cur = right[cur]
        steps += 1
            
    return steps
    
def part2():
    path_steps = []
    for node in starting:    
        path_steps.append(part1(node))
        
    print(np.array(path_steps))
    
    lcm = path_steps[0]
    for i in range(1, len(path_steps)):
        lcm = math.lcm(lcm, path_steps[i])
        
    return lcm
    
parse(inp)

print((starting))
# print(part1('AAA'))
print(part2())