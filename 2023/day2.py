import numpy as np

with open("day2.test") as f:
    fuck = f.readlines()

inp = []
for line in fuck:
    inp.append(line.strip("\n"))


def part1():
    limits = {"red": 12, "green": 13, "blue": 14}
    count = 0
    for index, line in enumerate(inp, start=1):
        l1 = line.split(": ")[1]
        pulls = l1.split("; ")
        good = True
        for pull in pulls:
            pairs = pull.split(", ")
            for item in pairs:
                color = item.split(" ")[1]
                value = int(item.split(" ")[0])
                if limits[color] < value:
                    good = False
                    break
        if good:
            count += index

    return count


def part2():
    maxes = {"red": 0, "green": 0, "blue": 0}
    count = 0
    for line in inp:
        maxes = {"red": 0, "green": 0, "blue": 0}
        l1 = line.split(": ")[1]
        pulls = l1.split("; ")
        for pull in pulls:
            pairs = pull.split(", ")
            for item in pairs:
                color = item.split(" ")[1]
                value = int(item.split(" ")[0])
                maxes[color] = max(maxes[color], value)

        count += maxes["red"] * maxes["green"] * maxes["blue"]

    return count


# print(part1())
print(part2())
