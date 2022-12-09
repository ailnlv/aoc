import sys

stacks = [list() for i in range(9)]

line = sys.stdin.readline()
while line[1] != '1':
    for i, letter in enumerate(line[1::4]):
        if letter == " ": continue
        stacks[i].insert(0, letter)
    line = sys.stdin.readline()

sys.stdin.readline()

for line in sys.stdin.readlines():
    move, fr, to = [int(x) for x in line.strip().split(" ")[1::2]]
    for _ in range(move):
        stacks[to - 1].append(stacks[fr - 1].pop())

print(stacks)
print(''.join([x[-1] for x in stacks]))
