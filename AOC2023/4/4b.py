file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

#indexed by 1 so Card i = cards[i]
cards = [0,1]
game = 1


for line in z.split('\n'):
    winningSet = []
    numbersSet = []
    winningNumbers = 0

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
            winningNumbers += 1
    if winningNumbers == 0:
        while game >= len(cards):
            cards.append(1)
    for i in range(1, winningNumbers+1):
        newCards = i + game
        while newCards >= len(cards):
            cards.append(1)
        cards[newCards] += cards[game]

    game += 1

#print(cards)
print(sum(cards))