import numpy as np

with open('day9.in') as f:
    fuck = f.readlines()

inp = []
for line in fuck:
    inp.append(line.strip('\n'))
    
starting_sequences = []
for line in inp:
    next_seq = []
    string_split = line.split(' ')
    for char in string_split:
        next_seq.append(int(char))
    starting_sequences.append(next_seq)
    
# print(starting_sequences)


def part1():
    out = 0
    for seq in starting_sequences:
        cur_seq = generate_sequences(seq)
        
        for i in range(len(cur_seq)-1, 0, -1):
            cur_seq[i-1].append(cur_seq[i-1][-1] + cur_seq[i][-1]) 
        out += cur_seq[0][-1]   
    return out  


def part2():
    out = 0
    for seq in starting_sequences:
        cur_seq = generate_sequences(seq)
        
        for i in range(len(cur_seq)-1, 0, -1):
            cur_seq[i-1].insert(0, cur_seq[i-1][0] - cur_seq[i][0]) 
            # print(cur_seq)
        out += cur_seq[0][0]   
        # print(cur_seq[0][0])
    return out  
        
        
def generate_sequences(start):
    cur_seq = [start]
    while True:
        next_seq = []
        terminated = True
        for i in range(1, len(cur_seq[-1])):
            num = cur_seq[-1][i] - cur_seq[-1][i-1]
            next_seq.append(num)
            if num != 0:
                terminated = False
        cur_seq.append(next_seq)
        # print(next_seq)
        if terminated:
            return cur_seq
        
# print(part1())
print(part2())