with open('in.txt') as f:
    lines = f.readlines()
    
# with open('test.txt') as f:
#     lines = f.readlines()
    
for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')
    

def part1():
    global lines
    
    count = 0
    
    for i in range(len(lines[0])):
        for j in range(len(lines)):
            try:
                num = int(lines[j][i])
                if adjacent_larger(i+1,j,num) and adjacent_larger(i-1,j,num) and adjacent_larger(i,j+1,num) and adjacent_larger(i,j-1,num):
                    print_area(i, j)
                    count += num + 1
            except RuntimeError as emsg:
                print(emsg)
                
                
                
    print(count)
    
def adjacent_larger(i, j, num):
    try:
        return num < int(lines[j][i])
    except:
        return True
    
def print_area(i, j):
    for ii in range(-1, 2):
        for jj in range(-1, 2):
            try:
                if ii == 0 and jj == 0:
                    print(lines[j + jj][i + ii], end = '< ')
                elif i + ii >= 0 and j + jj >= 0:
                    print(lines[j + jj][i + ii], end = ', ')
            except:
                pass
        print()
    print()
    
part1()

