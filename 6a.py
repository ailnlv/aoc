import sys

line = sys.stdin.readline()
for i in range(14, len(line)):
    if len(set(line[i-14:i])) == 14: break
print(i)

