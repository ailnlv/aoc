import fileinput

score = 0
for line in fileinput.input():
    if line.strip() == "": break
    left, right = line.strip().split(' ')
    left = ord(left) - ord('A')
    result = ord(right) - ord('X') - 1
    move = (left + result) % 3
    score += move + 1
    if result == 0:
        # tie
        score += 3
    if result == -1:
        # left won
        pass
    if result == 1:
        # right won
        score += 6
print(score)


