import numpy as np

with open("day15.in") as f:
    fuck = f.read()
inp = fuck.split(',')

def part1():
    hashes = []
    for item in inp:
        hashes.append(hash(item))
    return sum(hashes)

def hash(string):
    cur_value = 0
    for char in string:
        cur_value = ((cur_value + ord(char)) * 17) % 256
    return cur_value

def part2():
    lenses = [[] for _ in range(256)]
    labels = [[] for _ in range(256)]
    for item in inp:
        # print(item)
        if '=' in item:
            key = item[:-2]
            value = int(item[-1])
            ass = True
        else:
            key = item[:-1]
            ass = False
        index = hash(key)
        if ass:
            if key in labels[index]:
                remove_index = labels[index].index(key)
                lenses[index][remove_index] = value
            else:
                labels[index].append(key)
                lenses[index].append(value)
        else:
            if key in labels[index]:
                remove_index = labels[index].index(key)
                labels[index].pop(remove_index)
                lenses[index].pop(remove_index)
    # print(lenses)
    # print(labels)
    # print()
    
    count = 0
    for box_number, box in enumerate(lenses):
        for index, item in enumerate(box):
            count += (box_number+1) * item * (index + 1)
            # print((box_number+1) * item * (index + 1))
    return count

# print(part1())
print(part2())