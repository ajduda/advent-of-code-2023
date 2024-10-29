file = 'test.txt'
file = 'input.txt'

#awkwardly backwards sorted this :|
strengths = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

def handType(handTouple):
    hand = handTouple[0]
    items = dict()
    for c in hand:
        if c not in items:
            items[c] = 1
        else:
            items[c] += 1

    five = False
    four = False
    three = False
    two = False
    twoPair = False
    one = False

    for k in items.keys():
        match items[k]:
            case 5:
                five = True
            case 4:
                four = True
            case 3:
                three = True
            case 2:
                if two:
                    twoPair = True
                two = True
            case 1:
                one = True
    if five:
        return 1000
    if four:
        return 900
    if three and two:
        return 800
    if three:
        return 700
    if twoPair:
        return 600
    if two:
        return 500
    return 0


with open(file) as inp:
    z = inp.read()
    z = z.strip()

rank = 1
ans = 0

hands = []

for line in z.split('\n'):
    hand,score = line.split(' ')
    hands.append((hand,int(score)))

while len(hands) > 0:
    lowestHand = hands[0]
    lowestIndex = 0
    for i in range(1,len(hands)):
        currentHand = hands[i]

        lowestHandType = handType(lowestHand)
        currentHandType = handType(currentHand)
        
        if currentHandType < lowestHandType:
            lowestHand = currentHand
            lowestIndex = i
        elif currentHandType == lowestHandType:
            for c in range(0,5):
                if strengths.index(currentHand[0][c]) > strengths.index(lowestHand[0][c]):  # is lowest
                    lowestHand = currentHand
                    lowestIndex = i
                    break
                elif strengths.index(currentHand[0][c]) < strengths.index(lowestHand[0][c]):  # not lowest
                    break
                #else try next letter
    nextLowestHand = hands.pop(lowestIndex)
    ans += nextLowestHand[1] * rank
    rank += 1

print(ans)
