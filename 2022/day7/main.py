def main():
    global root
    global lines
    global cur_line
    global outer
    global overall_size
    global total_file_size
    global min_valid_dir
    global required_space
    cur_line = 0
    lines = read('in.txt')
    # print(lines)
    root = Node(0, None, '/', 'dir')
    outer = root
    while cur_line < len(lines):
        # print(lines[cur_line])
        run_command(lines[cur_line])
        cur_line += 1
    print('='*32)
    visualize(outer)
    print('='*32)

    total_file_size = outer.get_size()

    free_space = 70000000 - total_file_size

    required_space = 30000000 - free_space

    min_valid_dir = total_file_size

    print('total', total_file_size)
    print('required', required_space)
    overall_size = 0
    dir_under_100k(outer)

    print('overall', overall_size)
    smallest_valid_dir(outer)
    print('min_valid_dir', min_valid_dir)


def run_command(command):
    global root
    # print(root.name)
    command = command.split(' ')
    if command[0] == '$':
        if command[1] == 'cd':
            if command[2] == '..':
                root = root.get_parent()
            elif command[2] == '/':
                root = outer
            else:
                root = root.get_child(command[2])
        elif command[1] == 'ls':
            read_ls()


def read_ls():
    global cur_line
    global root
    cur_line += 1
    line = lines[cur_line]
    while line[0] != '$' and cur_line < len(lines):
        # print(line)
        command = line.split(' ')
        if command[0] == 'dir':
            root.add_child(Node(0, root, command[1], 'dir'))
        else:
            root.add_child(Node(command[0], root, command[1], 'file'))
        cur_line += 1
        if cur_line >= len(lines):
            break
        line = lines[cur_line]
    cur_line -= 1


class Node:
    def __init__(self, size=0, parent=None, name='', type='file'):
        self.size = int(size)
        self.parent = parent
        self.name = name
        self.type = type
        self.children = []

    def get_size(self):
        for child in self.children:
            self.size += child.get_size()
        return self.size

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child

    def add_child(self, child):
        self.children.append(child)

    def get_parent(self):
        return self.parent


def visualize(root, level=0):
    if root.type == 'dir':
        print(f'{"  "*level}- {root.name} (dir)')
    else:
        print(f'{"  "*level}- {root.name} ({root.type}, size={root.size})')
    for child in root.children:
        visualize(child, level+1)


def dir_under_100k(root):
    global overall_size
    total_size = root.size
    # print(root.name, root.size)
    for child in root.children:
        if child.type == 'dir':
            # total_size += child.size
            dir_under_100k(child)
    # print(root.name, total_size)
    if total_size < 100000:
        overall_size += total_size


def smallest_valid_dir(root):
    global min_valid_dir
    # print(root.name, root.size)
    if root.size >= required_space and root.size < min_valid_dir:
        # print(root.name, root.size)
        min_valid_dir = root.size
    # print(root.name, root.size)
    for child in root.children:
        if child.type == 'dir':
            # total_size += child.size
            smallest_valid_dir(child)
        # print(root.name, total_size)


def read(file):
    with open(file) as f:
        lines = f.readlines()
    fixed = []
    for line in lines:
        fixed.append(line.removesuffix('\n'))
    return fixed


main()
