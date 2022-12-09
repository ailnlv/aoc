import fileinput
import re
count = 0

for line in fileinput.input():
    l1, l2, r1, r2 = [int(x) for x in re.split(r"[-,]", line.strip())]
    assert(l1 <= l2 and r1 <= r2)
    if (l1 <= r1 and l2 >= r2) or (l1 >= r1 and l2 <= r2):
        count += 1


print(count)
