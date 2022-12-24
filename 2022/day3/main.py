with open('in.txt') as f:
    lines = f.readlines()

fixed = []
for line in lines:
    fixed.append(line.removesuffix('\n').strip())

# print(fixed[0][:len(fixed[0])//2], fixed[0][len(fixed[0])//2:], sep='\n')
# print(fixed[0])
items = []
for line in fixed:
    line1 = line[:len(line)//2]
    line2 = line[len(line)//2:]

    for item in line1:
        if item in line2:
            items.append(item)
            break

# print(items)

key = '-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0
for item in items:
    total += key.index(item)

print(total)


items = []
for i in range(0, len(fixed), 3):
    line1 = fixed[i]
    line2 = fixed[i+1]
    line3 = fixed[i+2]

    potential_items = []

    for item in line1:
        if item in line2:
            potential_items.append(item)

    for item in line3:
        if item in potential_items:
            items.append(item)
            break

# print(items)

key = '-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0
for item in items:
    total += key.index(item)

print(total)
