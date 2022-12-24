def main():
    global visited_points
    global cur_head
    global cur_tail
    visited_points = [(0, 0)]
    cur_tail = [0, 0]
    cur_head = [0, 0]
    lines = read('in.txt')
    for line in lines:
        step(line.split()[0], int(line.split()[1]))
    print(len(visited_points))


def step(dir, dist):
    global cur_tail
    global cur_head
    global visited_points
    for _ in range(dist):
        if dir == 'U':
            cur_head[1] += 1
        elif dir == 'D':
            cur_head[1] -= 1
        elif dir == 'R':
            cur_head[0] += 1
        elif dir == 'L':
            cur_head[0] -= 1

        if not is_tail_close():
            cur_tail = cur_head.copy()
            if dir == 'U':
                cur_tail[1] -= 1
            elif dir == 'D':
                cur_tail[1] += 1
            elif dir == 'R':
                cur_tail[0] -= 1
            elif dir == 'L':
                cur_tail[0] += 1

            if cur_tail not in visited_points:
                visited_points.append(cur_tail)


def is_tail_close():
    return cur_tail[0] - cur_head[0] in [-1, 0, 1] and cur_tail[1] - cur_head[1] in [-1, 0, 1]


def read(file):
    with open(file) as f:
        lines = f.readlines()
    fixed = []
    for line in lines:
        fixed.append(line.removesuffix('\n'))
    return fixed


main()
