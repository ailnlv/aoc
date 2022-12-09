import fileinput
import re
count = 0

for line in fileinput.input():
    l1, l2, r1, r2 = [int(x) for x in re.split(r"[-,]", line.strip())]
    if (l1 <= r1 <= l2 or l1 <= r2 <= l2 or r1 <= l1 <= r2 or r1 <= l2 <= r2):
        count += 1

print(count)
