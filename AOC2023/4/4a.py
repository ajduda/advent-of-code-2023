file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    winningSet = []
    numbersSet = []
    cardVal = 0

    left, right = line.split(' | ')
    winning = left.split(' ')
    winning = winning[2:]
    numbers = right.split(' ')

    for w in winning:
        if len(w) == 0:
            continue
        elif w[-1] == ':':
            continue
        winningSet.append(int(w))

    for n in numbers:
        if len(n) == 0:
            continue
        if int(n) in winningSet:
            if cardVal == 0:
                cardVal = 1
            else:
                cardVal *= 2

    ans += cardVal

print(ans)