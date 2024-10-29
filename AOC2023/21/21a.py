file,STEPS = 'test.txt',6
#file,STEPS = 'input.txt',66

with open(file) as inp:
    z = inp.read()
    z = z.strip()


rocks = set()
possible = set()
y = 0
for line in z.split('\n'):
    x = 0
    for c in line:
        if c == 'S':
            possible.add((y,x))
        if c == '#':
            rocks.add((y,x))
        x += 1
    y += 1

maxX = x + 1
maxY = y + 1

print(maxX)
print(maxY)

#I found from testing part B and not getting the expected difference, that partA isn't bounded correctly and would fail.
#maxX, maxY would need to -1 instead of +1 to fix this
for i in range(0,STEPS):
    nextPossible = set()
    for (y,x) in possible:
        if y < maxY and (y+1,x) not in rocks:
            nextPossible.add((y+1,x))
        if y > 0 and (y-1,x) not in rocks:
            nextPossible.add((y-1,x))
        if x < maxX and (y,x+1) not in rocks:
            nextPossible.add((y,x+1))
        if x > 0 and (y,x-1) not in rocks:
            nextPossible.add((y,x-1))
    possible = nextPossible

print(len(nextPossible))