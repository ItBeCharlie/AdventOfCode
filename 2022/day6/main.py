with open('in.txt') as f:
    lines = f.readlines()

line = lines[0]

print(line[1615:1625])

for i in range(len(line)):
    crib = line[i:i+14]
    items = []
    good_crib = True
    for item in crib:
        if item in items:
            good_crib = False
            break
        items.append(item)
    if good_crib:
        print(i+14)
        break
