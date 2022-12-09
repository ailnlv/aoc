import sys
import re

root = dict(files=0, children=dict())
curr = root
for line in sys.stdin.readlines():
    line = line.strip()
    if line == "$ cd /":
        curr = root
    elif line.startswith("$ cd"):
        curr = curr['children'][line.split(' ')[-1]]
    elif line.startswith("dir"):
        curr['children'][line.split(" ")[-1]] = {'files': 0, 'children': {'..': curr}}
    elif re.match("^\d+", line):
        curr['files'] += int(line.split(" ")[0])
    elif line.startswith("$ ls"): continue
    else:
        print(line)
        break

sizes = []
def recurse(node):
    global sizes
    size = node['files'] + sum(recurse(child) for k, child in node['children'].items() if k != "..")
    sizes.append(size)
    return size
space_needed = 30000000 + recurse(root) - 70000000
sizes.sort()

print(space_needed, sizes)
import bisect
i = bisect.bisect_left(sizes, space_needed)
print(sizes[i])

