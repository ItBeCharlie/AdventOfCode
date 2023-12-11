import numpy as np

with open('day7.test') as f:
    fuck = f.readlines()
    
old_values = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
new_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 11, 'K': 12, 'A': 13}

hands = []
for line in fuck:
    hands.append(line.strip('\n').split(' '))
# print(inp)

# print(hands)

def part1():
    for i in range(len(hands)-1):
        for j in range(len(hands)-1):
            swap = False
            hand1 = hands[j][0]
            hand2 = hands[j+1][0]
            rank1 = rank_hand(hand1)
            rank2 = rank_hand(hand2)
            if rank1 < rank2:
                swap = True
            elif rank1 == rank2:
                # print(hand1, hand2)
                for index, _ in enumerate(hand1):
                    # print(index, hand1[index], hand2[index])
                    if old_values[hand1[index]] == old_values[hand2[index]]:
                        continue
                    if old_values[hand1[index]] < old_values[hand2[index]]:
                        swap = True
                    break
                # print(swap)
            if swap:
                hands[j], hands[j+1] = hands[j+1], hands[j]
                
    print(hands)
    score = 0
    for index, hand in enumerate(hands):
        score += int(hand[1]) * (len(hands) - index)
    return score


def part2():
    for i in range(len(hands)-1):
        for j in range(len(hands)-1):
            swap = False
            hand1 = hands[j][0]
            hand2 = hands[j+1][0]
            rank1 = new_rank_hand(hand1)
            rank2 = new_rank_hand(hand2)
            if rank1 < rank2:
                swap = True
            elif rank1 == rank2:
                # print(hand1, hand2)
                for index, _ in enumerate(hand1):
                    # print(index, hand1[index], hand2[index])
                    if new_values[hand1[index]] == new_values[hand2[index]]:
                        continue
                    if new_values[hand1[index]] < new_values[hand2[index]]:
                        swap = True
                    break
                # print(swap)
            if swap:
                hands[j], hands[j+1] = hands[j+1], hands[j]
                
    print(hands)
    score = 0
    for index, hand in enumerate(hands):
        score += int(hand[1]) * (len(hands) - index)
    return score


def rank_hand(hand):
    counts = {}
    for value in hand:
        if value not in counts:
            counts[value] = 0
        counts[value] += 1
    # print(mult, counts)
    count_old_values = list(counts.values())
    if 5 in count_old_values:
        return 7
    if 4 in count_old_values:
        return 6
    if 3 in count_old_values and 2 in count_old_values:
        return 5
    if 3 in count_old_values:
        return 4
    two_count = 0
    for value in count_old_values:
        if value == 2:
            two_count += 1
    return two_count + 1


def new_rank_hand(hand):
    # ['JJQJA', '446'], ['JJTTT', '907']
    counts = {}
    j_count = 0
    for value in hand:
        if value not in counts:
            if value != 'J':
                counts[value] = 1
            else:
                j_count += 1
        else:
            counts[value] += 1
        
    # print(mult, counts)
    count_old_values = list(counts.values())
    two_count = 0
    for value in count_old_values:
        if value == 2:
            two_count += 1
    if 5 in count_old_values or (4 in count_old_values and j_count >= 1) or (3 in count_old_values and j_count >= 2) or (2 in count_old_values and j_count >= 3) or (j_count >= 4):
        return 7
    if 4 in count_old_values or (3 in count_old_values and j_count >= 1) or (2 in count_old_values and j_count >= 2) or (j_count >= 3):
        return 6
    if (3 in count_old_values and 2 in count_old_values) or (two_count == 2 and j_count >= 1):
        return 5
    if 3 in count_old_values or (two_count == 1 and j_count == 1):
        return 4
    if two_count == 2:
        return 3
    if two_count == 1 or j_count >= 1:
        return 2
    return 1
    
    
# print(part1())
print(part2())