with open('in.txt') as f:
    lines = f.readlines()
    
# with open('test.txt') as f:
#     lines = f.readlines()
    
g = 0
e = 0

g_b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# g_b = [0, 0, 0, 0, 0]
e_b = g_b.copy()

def part1():
    for line in lines:
        for i in range(len(line)-1):
            if line[i] == '1':
                g_b[i] += 1
                e_b[i] -= 1 
            elif line[i] == '0':
                g_b[i] -= 1
                e_b[i] += 1 
            
    g_str = ''
    e_str = ''
                
    for i in g_b:
        g_str += str(min(1, max(0, i)))
        
    for i in e_b:
        e_str += str(min(1, max(0, i)))
        
    print(g_str)

    g = int(g_str, 2)

    print(e_str)

    e = int(e_str, 2)

    print()

    pc = g * e

    print(pc)

def part2():
    global lines
    
    one_list = []
    zero_list = []
    
    line_save = lines.copy()
        
    for bit in range(len(lines[0])-1):
        # print(lines)
        one_list = []
        zero_list = []
        for line in lines:    
            if line[bit] == '1':
                one_list.append(line)
            elif line[bit] == '0':
                zero_list.append(line)
        if len(one_list) >= len(zero_list):
            lines = one_list.copy()
        else:
            lines = zero_list.copy()
            
    print(lines[0])
    
    o2 = lines[0]
    
    lines = line_save.copy()
    
    for bit in range(len(lines[0])-1):
        # print(lines)
        one_list = []
        zero_list = []
        for line in lines:    
            if line[bit] == '1':
                one_list.append(line)
            elif line[bit] == '0':
                zero_list.append(line)
        if len(lines) > 1:
            if len(zero_list) <= len(one_list):
                lines = zero_list.copy()
            else:
                lines = one_list.copy()
        
            
    print(lines[0])
    
    co2 = lines[0]
    
    print(int(o2, 2) * int(co2, 2))
        
            
        
        
        

# part1()
part2()