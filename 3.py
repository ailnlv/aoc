import fileinput

priorities = 0
for line in fileinput.input():
    left = set(line[:len(line) // 2])
    right = set(line[len(line) // 2:])
    dupes = left.intersection(right)
    for char in dupes:
        if ord(char) < ord('a'):
            priorities += ord(char) - ord('A') + 27
        else:
            priorities += ord(char) - ord('a') + 1
print(priorities)
