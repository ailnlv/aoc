import sys

priorities = 0

while True:
    elves = [set(sys.stdin.readline().strip()) for x in range(3)]
    if len(elves[0]) == 0:
        break
    char = elves[0].intersection(elves[1]).intersection(elves[2])
    char = list(char)[0]

    if ord(char) < ord('a'):
        priorities += ord(char) - ord('A') + 27
    else:
        priorities += ord(char) - ord('a') + 1
print(priorities)
