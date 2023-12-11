import numpy as np

with open('day4.in') as f:
    fuck = f.readlines()

inp = []
for line in fuck:
    inp.append(line[5:].strip('\n'))
# print(inp)

winning = []
scratch = []

for line in inp:
    ignore_card = line.split(': ')[1]
    win = ignore_card.split(' | ')[0].split(' ')
    scr = ignore_card.split(' | ')[1].split(' ')
    # print(win)
    # print(scr)
    temp = []
    for item in win:
        if item != '':
            temp.append(int(item))
    winning.append(temp)
    temp = []
    for item in scr:
        if item != '':
            temp.append(int(item))
    scratch.append(temp)

# print(winning)
# print(scratch)
    
def part1():
    wins = []
    for i in range(len(scratch)):
        count = 1
        for num in scratch[i]:
            if num in winning[i]:
                count *= 2
        wins.append(count // 2)
    # print(wins)
    return sum(wins)
    
print(part1())