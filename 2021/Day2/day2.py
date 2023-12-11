with open('day2in.txt') as f:
    lines = f.readlines()
    
# with open('day2test.txt') as f:
#     lines = f.readlines()

h = 0
v = 0
aim = 0
    

for line in lines:
    if len(line) != 1:
        if 'forward' in line:
            h += int(line[-2])
            v += aim * int(line[-2])
        if 'up' in line:
            aim -= int(line[-2])
        if 'down' in line:
            aim += int(line[-2])
    
        
print(h*v, h, v)