import numpy as np

with open('day3.in') as f:
    fuck = f.readlines()

inp = []
for line in fuck:
    inp.append(line.strip('\n'))
# print(inp)


def convert_to_list_1(lines):
    out = [[0 for _ in range(len(lines))] for _ in range(len(lines[0]))]
    total = 0
    num = ''
    for i in range(len(lines)):
        if num != '':
            for k in range(len(num)):
                out[i-1][len(lines[i])-k-1] = int(num)
            total += int(num)
            num = ''
            
        for j in range(len(lines[i])):
            if lines[i][j] in '1234567890':
                num += lines[i][j]
            elif num != '':
                for k in range(len(num)):
                    out[i][j-k-1] = int(num)
                total += int(num)
                num = ''
            if lines[i][j] != '.':
                out[i][j] = -1
    return out, total

def convert_to_list_2(lines):
    out = [[0 for _ in range(len(lines))] for _ in range(len(lines[0]))]
    total = 0
    num = ''
    for i in range(len(lines)):
        if num != '':
            for k in range(len(num)):
                out[i-1][len(lines[i])-k-1] = int(num)
            total += int(num)
            num = ''
            
        for j in range(len(lines[i])):
            if lines[i][j] in '1234567890':
                num += lines[i][j]
            elif num != '':
                for k in range(len(num)):
                    out[i][j-k-1] = int(num)
                total += int(num)
                num = ''
            if lines[i][j] == '*':
                out[i][j] = -1
    return out, total


def part1():
    matrix, total = convert_to_list_1(inp)
    print(np.array(matrix))
    print(total)

    for i in range(len(matrix)):
        j = 0
        while j < len(matrix[i]):
            if matrix[i][j] > 0:
                real_part = False
                for k in range(len(str(matrix[i][j]))):  
                    if not check_empty_around(matrix, j+k, i):
                        real_part = True
                # print(real_part)
                if not real_part:
                    total -= matrix[i][j]
                    print(matrix[i][j])
                j += len(str(matrix[i][j]))
            else:
                j += 1
    return total


def part2():
    matrix, _ = convert_to_list_2(inp)
    print(np.array(matrix))
    # print(total)

    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == -1:
                count += get_product_around(matrix, j, i)
                
    return count


def check_empty_around(matrix, x, y):
    for i in range(-1 + y, 2 + y):
        for j in range(-1 + x, 2 + x):
            if i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[i]):
                # print(i, j, matrix[y][x], matrix[i][j])
                if matrix[i][j] == -1:
                    return False
    return True


def get_product_around(matrix, x, y):
    seen = []
    for i in range(-1 + y, 2 + y):
        for j in range(-1 + x, 2 + x):
            if i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[i]):
                # print(i, j, matrix[y][x], matrix[i][j])
                if matrix[i][j] > 0 and matrix[i][j] not in seen:
                    seen.append(matrix[i][j])
    product = 1
    if len(seen) < 2:
        return 0
    for item in seen:
        product *= item
    return product


# print(part1())
print(part2())

