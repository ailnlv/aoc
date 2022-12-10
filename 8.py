import sys
import re

grid = []
for line in sys.stdin.readlines():
    grid.append([int(x) for x in line.strip()])

visible_set = set()

maxtrees_row = [-1] * len(grid[0])
for i, row in enumerate(grid):
    maxtree_side = -1
    for j, t in enumerate(row):
        if t > maxtree_side:
            maxtree_side = t
            visible_set.add((i, j))
        if t > maxtrees_row[j]:
            maxtrees_row[j] = t
            visible_set.add((i, j))


maxtrees_row = [-1] * len(grid[0])
for i, row in reversed(list(enumerate(grid))):
    maxtree_side = -1
    for j, t in reversed(list(enumerate(row))):
        if t > maxtree_side:
            maxtree_side = t
            visible_set.add((i, j))
        if t > maxtrees_row[j]:
            maxtrees_row[j] = t
            visible_set.add((i, j))
print(len(visible_set))

