file = 'test.txt'  # test input was modified to have the same breakaway directions from the start like the input
file = 'input.txt'

STEPS = 26501365

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
            snapshotMod = y
        if c == '#':
            rocks.add((y,x))
        x += 1
    y += 1

mod = y

#A copy of part A to compare to part B to ensure rock modulous was working fine.
"""
maxX = x-1
maxY = y-1


possibleA = possible.copy()
for i in range(0,STEPS):
    nextPossible = set()
    for (y,x) in possibleA:
        if y < maxY and (y+1,x) not in rocks:
            nextPossible.add((y+1,x))
        if y > 0 and (y-1,x) not in rocks:
            nextPossible.add((y-1,x))
        if x < maxX and (y,x+1) not in rocks:
            nextPossible.add((y,x+1))
        if x > 0 and (y,x-1) not in rocks:
            nextPossible.add((y,x-1))
    possibleA = nextPossible
"""
#part B proper
#STEPS += mod*3 + 1
iterations = snapshotMod + mod*3
snapshots = []


for i in range(0,iterations+1):
    if i % mod == snapshotMod:
        print(i)
        snapshots.append(len(possible))
    nextPossible = set()
    for (y,x) in possible:
        if ((y+1)%mod,x%mod) not in rocks:
            nextPossible.add((y+1,x))
        if ((y-1)%mod,x%mod) not in rocks:
            nextPossible.add((y-1,x))
        if (y%mod,(x+1)%mod) not in rocks:
            nextPossible.add((y,x+1))
        if (y%mod,(x-1)%mod) not in rocks:
            nextPossible.add((y,x-1))
    possible = nextPossible

#printing to figure out where I went wrong in part B. Turns out B was working and A didn't work for cases bigger than the size
"""
for y in range(-15,20):
    s = ''
    for x in range(-15,20):
        if (y%mod,x%mod) in rocks:
            s += '#'
        elif (y,x) in possibleA:
            s += 'A'
        elif (y,x) in possible:
            s += 'B'
        else:
            s += ' '
    print(s)

print(possibleA - possible)  #If this is not set(), I have some real issues
print(possible - possibleA)
"""
numbers = []
while len(snapshots) > 1:
    print(snapshots)
    numbers.append(snapshots[-1])
    nextSnapshots = []
    for i in range(len(snapshots)-1):
        nextSnapshots.append(snapshots[i+1]-snapshots[i])
    snapshots = nextSnapshots


chunksRemaining = (STEPS-iterations) // mod

p = numbers[0]
v = numbers[1]
a = numbers[2]

for i in range(chunksRemaining):
    v += a
    p += v

print(p)