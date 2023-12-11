with open('day1in.txt') as f:
    lines = f.readlines()
    
count = 0
last_num = int(lines[0])

for line in lines:
    if int(line) > last_num:
        count += 1
    last_num = int(line)

print(count)


count = 0
last_num = int(lines[0]) + int(lines[1]) + int(lines[2])

i = 1
while i < (len(lines)-2):
    if int(lines[i]) + int(lines[i+1]) + int(lines[i+2]) > last_num:
        count += 1
    last_num = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    i += 1

print(count)