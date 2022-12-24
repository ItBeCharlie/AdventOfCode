with open('in.txt') as f:
    lines = f.readlines()
fixed = []
for line in lines:
    fixed.append(line.replace(',', '-').removesuffix('\n').split('-'))

count = 0
for line in fixed:
    if (int(line[0]) <= int(line[2]) and int(line[1]) >= int(line[3])) or (int(line[0]) >= int(line[2]) and int(line[1]) <= int(line[3])):
        count += 1
        # print(line)
print(count)

count = 0
for line in fixed:
    if (int(line[0]) < int(line[2]) and int(line[1]) < int(line[2])) or (int(line[2]) < int(line[0]) and int(line[3]) < int(line[0])):
        pass
    else:
        count += 1
        # print(line)
print(count)
