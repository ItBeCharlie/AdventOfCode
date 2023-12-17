import numpy as np

with open("day13.in") as f:
    fuck = f.readlines()

grid = []
for line in fuck:
    grid.append(line.strip("\n"))   