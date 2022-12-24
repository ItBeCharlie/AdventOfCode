def main():
    lines = read('in.txt')
    score = 0
    for line in lines:
        score += win_points(line)
        if line[2] == 'X':
            score += 1
        elif line[2] == 'Y':
            score += 2
        elif line[2] == 'Z':
            score += 3
    print(score)

    score = 0
    for line in lines:
        score += part_2(line)
    print(score)


def win_points(choice):
    if choice[0] == 'A':
        if choice[2] == 'X':
            return 3
        elif choice[2] == 'Y':
            return 6
        elif choice[2] == 'Z':
            return 0
    elif choice[0] == 'B':
        if choice[2] == 'X':
            return 0
        elif choice[2] == 'Y':
            return 3
        elif choice[2] == 'Z':
            return 6
    elif choice[0] == 'C':
        if choice[2] == 'X':
            return 6
        elif choice[2] == 'Y':
            return 0
        elif choice[2] == 'Z':
            return 3


def part_2(choice):
    if choice[2] == 'X':
        if choice[0] == 'A':
            return 3
        elif choice[0] == 'B':
            return 1
        elif choice[0] == 'C':
            return 2
    if choice[2] == 'Y':
        if choice[0] == 'A':
            return 1 + 3
        elif choice[0] == 'B':
            return 2 + 3
        elif choice[0] == 'C':
            return 3 + 3
    if choice[2] == 'Z':
        if choice[0] == 'A':
            return 2 + 6
        elif choice[0] == 'B':
            return 3 + 6
        elif choice[0] == 'C':
            return 1 + 6


def read(file):
    with open(file) as f:
        lines = f.readlines()
    fixed = []
    for line in lines:
        fixed.append(line.removesuffix('\n'))
    return fixed


main()
