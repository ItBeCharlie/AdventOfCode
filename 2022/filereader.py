def read(file):
    with open(file) as f:
        lines = f.readlines()
    fixed = []
    for line in lines:
        fixed.append(line.removesuffix('\n'))
    return fixed
