import enum


with open('day3in.txt') as f:
    lines = f.readlines()


def is_tri(vals):
    max_val = max(vals)
    vals.remove(max_val)
    return vals[0] + vals[1] > max_val


count = 0
for line in lines:
    str_vals = line.replace('\n', '').split()
    vals = [eval(i) for i in str_vals]
    if is_tri(vals):
        count += 1
        # print(vals, max_val)
print(count)

count = 0

line_buf = []
for index, line in enumerate(lines, 1):
    line_buf.append(line.replace('\n', '').split())
    if index % 3 == 0:
        for i in range(3):
            if is_tri([int(line_buf[0][i]), int(line_buf[1][i]), int(line_buf[2][i])]):
                count += 1
        line_buf = []

print(count)
