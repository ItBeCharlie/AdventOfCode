def main():
    global grid
    global state
    with open('in.txt') as f:
        lines = f.readlines()

    grid = []

    for line in lines:
        grid.append(line.removesuffix('\n'))

    print(grid)

    state = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    count = 0
    for i in range(len(grid)):
        count += traverse_column(i) + traverse_column_backwards(i) + \
            traverse_line(i) + traverse_line_backwards(i)
        # print_state()

    print_state()
    print(count)

    max_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            cur_tree = grid[i][j]
            score = 1
            # up
            count = 0
            for k in range(i-1, -1, -1):
                count += 1
                if grid[k][j] >= cur_tree:
                    break

            score *= count

            # down
            count = 0
            for k in range(i+1, len(grid)):
                count += 1
                if grid[k][j] >= cur_tree:
                    break

            score *= count

            # left
            count = 0
            for k in range(j-1, -1, -1):
                count += 1
                if grid[i][k] >= cur_tree:
                    break

            score *= count

            # right
            count = 0
            for k in range(j+1, len(grid[i])):
                count += 1
                if grid[i][k] >= cur_tree:
                    break

            score *= count

            if score > max_score:
                max_score = score
                max_point = [i, j]
    print(max_score, max_point)


def traverse_line(index):
    max_tree = -1
    count = 0
    for i in range(len(grid[index])):
        tree = int(grid[index][i])
        if tree > max_tree:
            if not state[index][i]:
                count += 1
                state[index][i] = True
            max_tree = tree

    return count


def traverse_line_backwards(index):
    max_tree = -1
    count = 0
    for i in range(len(grid[index])-1, -1, -1):
        tree = int(grid[index][i])
        if tree > max_tree:
            if not state[index][i]:
                count += 1
                state[index][i] = True
            max_tree = tree

    return count


def traverse_column(index):
    max_tree = -1
    count = 0
    for i in range(len(grid)):
        tree = int(grid[i][index])
        if tree > max_tree:
            if not state[i][index]:
                count += 1
                state[i][index] = True
            max_tree = tree
    return count


def traverse_column_backwards(index):
    max_tree = -1
    count = 0
    for i in range(len(grid)-1, -1, -1):
        tree = int(grid[i][index])
        if tree > max_tree:
            if not state[i][index]:
                count += 1
                state[i][index] = True
            max_tree = tree
    return count


def print_state():
    for i in state:
        for j in i:
            if j:
                print('x', end='')
            else:
                print('_', end='')
        print()


main()
