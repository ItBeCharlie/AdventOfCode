from copy import deepcopy

with open('in.txt') as f:
    lines = f.readlines()

# print(lines[:10])

cur_index = 0
line = lines[cur_index]

stacks = [[] for _ in range(10)]
# print(stacks)
stacks[0].append('')

while line[1] != '1':
    for i in range(1, len(line), 4):
        if line[i] != ' ':
            stacks[i//4 + 1].insert(0, line[i])

    cur_index += 1
    line = lines[cur_index]

orig_stacks = deepcopy(stacks)

# print(stacks)
instructions = []

for i in range(cur_index+2, len(lines)):
    sp = lines[i].split(' ')
    instructions.append([int(sp[1]), int(sp[3]), int(sp[5])])

# print(instructions)

for command in instructions:
    for _ in range(command[0]):
        stacks[command[2]].append(stacks[command[1]].pop())


out = ''
for item in stacks:
    out += item.pop()
print(out)

stacks = deepcopy(orig_stacks)
# print(stacks)

for command in instructions:
    # print(command[0], stacks[command[1]], stacks[command[2]])
    stacks[command[2]].extend(stacks[command[1]][-command[0]:])
    stacks[command[1]] = stacks[command[1]][:-command[0]]
    # print(command[0], stacks[command[1]], stacks[command[2]])
    # print()

# print(stacks)
out = ''
for item in stacks:
    if (len(item) != 0):
        out += item.pop()
    else:
        out += ' '
print(out)
