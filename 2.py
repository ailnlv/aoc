import fileinput

score = 0
for line in fileinput.input():
    if line.strip() == "": break
    left, right = line.strip().split(' ')
    left = ord(left) - ord('A')
    right = ord(right) - ord('X')
    result = (left - right) % 3
    score += right + 1
    if result == 0:
        # tie
        score += 3
    if result == 1:
        # left won
        pass
    if result == 2:
        # right won
        score += 6
print(score)


