with open('in.txt') as f:
    lines = f.readlines()

calories = [0, 0, 0]
cur_sum = 0
for line in lines:
    if line == '\n':
        if calories[0] < cur_sum:
            calories[2] = calories[1]
            calories[1] = calories[0]
            calories[0] = cur_sum
        elif calories[1] < cur_sum:
            calories[2] = calories[1]
            calories[1] = cur_sum
        elif calories[2] < cur_sum:
            calories[2] = cur_sum
        cur_sum = 0
    else:
        cur_sum += int(line)
print(calories)
print(calories[0])
print(sum(calories))
