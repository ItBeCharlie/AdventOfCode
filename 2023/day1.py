with open('day1.in') as f:
    fuck = f.readlines()

inp = []
for line in fuck:
    inp.append(line.strip('\n'))


def part1(lines):
    count = 0
    for line in lines:
        for char in line:
            if char in '1234567890':
                count += int(char) * 10
                break
        line = reversed(line)
        for char in line:
            if char in '1234567890':
                count += int(char)
                break
    return count


def part2(lines):
    count = 0
    for line in lines:
        i = 0
        print('f')
        print(line)
        while i < len(lines):
            check5 = line[i:i+5]
            check4 = line[i:i+4]
            check3 = line[i:i+3]
            # print(check)
            if line[i] in '1234567890':
                count += int(line[i]) * 10
                break
            elif 'zero' in check4:
                count += 0 * 10
                break
            elif 'one' in check3:
                count += 1 * 10
                break
            elif 'two' in check3:
                count += 2 * 10
                break
            elif 'three' in check5:
                count += 3 * 10
                break
            elif 'four' in check4:
                count += 4 * 10
                break
            elif 'five' in check4:
                count += 5 * 10
                break
            elif 'six' in check3:
                count += 6 * 10
                break
            elif 'seven' in check5:
                count += 7 * 10
                break
            elif 'eight' in check5:
                count += 8 * 10
                break
            elif 'nine' in check4:
                count += 9 * 10
                break
            i += 1
        line = line[::-1]
        print(count)
        print('b')
        print(line)
        i = 0
        while i < len(lines):

            check5 = line[i:i+5]
            check4 = line[i:i+4]
            check3 = line[i:i+3]
            # print(check4)
            if line[i] in '1234567890':
                count += int(line[i]) * 1
                break
            elif 'orez' in check4:
                count += 0 * 1
                break
            elif 'eno' in check3:
                count += 1 * 1
                break
            elif 'owt' in check3:
                count += 2 * 1
                break
            elif 'eerht' in check5:
                count += 3 * 1
                break
            elif 'ruof' in check4:
                count += 4 * 1
                break
            elif 'evif' in check4:
                count += 5 * 1
                break
            elif 'xis' in check3:
                count += 6 * 1
                break
            elif 'neves' in check5:
                count += 7 * 1
                break
            elif 'thgie' in check5:
                count += 8 * 1
                break
            elif 'enin' in check4:
                count += 9 * 1
                break
            i += 1
        print(count)
        print()
    return count


# print(part1(inp))
print(part2(inp))
