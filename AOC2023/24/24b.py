file = 'test.txt'
file = 'input.txt'

PRIMEBOUND = 2000 # calculate primes up to this number

primes = []

checkPrimes = []
for i in range(0,PRIMEBOUND):
    checkPrimes.append(True)

i = 2
while i*i < PRIMEBOUND:
    if checkPrimes[i]:
        j = i + i
        while j < PRIMEBOUND:
            checkPrimes[j] = False
            j += i
    i += 1

primes = []
for i in range(2,PRIMEBOUND):
    if checkPrimes[i]:
        primes.append(i)

lines = []


def validVelocities(p1,p2,baseSpeed):
    diff = abs(p1-p2)
    primeFactors = []
    i = 0
    while primes[i]*primes[i] <= diff:
        if diff % primes[i] == 0:
            primeFactors.append(primes[i])
            diff //= primes[i]
        else:
            i += 1
            if i == len(primes):
                break
    if diff > 1:  # in case we get a prime bigger than I calculated for
        primeFactors.append(diff)

    maxPrimes = {}  # count the max exponent of all primes present
    for n in primeFactors:
        if n not in maxPrimes:
            maxPrimes[n] = 1
        else:
            maxPrimes[n] += 1

    primeIndexes = []   # which prime does currentIndexes[i] refer to at index i?
    currentIndexes = [] # what is the exponent of the i'th prime in this number?
    for n in maxPrimes:
        if n not in primeIndexes:
            primeIndexes.append(n)
            currentIndexes.append(0)

    factors = set()

    while True:  # will break when finished
        product = 1
        for i in range(0,len(primeIndexes)):
            product *= (primeIndexes[i] ** currentIndexes[i])
        factors.add(product)
        i = 0
        while i < len(primeIndexes):
            currentIndexes[i] += 1
            if currentIndexes[i] > maxPrimes[primeIndexes[i]]:
                currentIndexes[i] = 0
                i += 1
            else:
                break
        if i == len(primeIndexes):
            break

    possibleVelocities = set()
    for n in factors:
        possibleVelocities.add(baseSpeed + n)
        possibleVelocities.add(baseSpeed - n)

    return possibleVelocities


with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    px,py,pz,_,dx,dy,dz = line.split(' ')
    px = int(px[:-1])
    py = int(py[:-1])
    pz = int(pz)
    dx = int(dx[:-1])
    dy = int(dy[:-1])
    dz = int(dz)
    lines.append((px,py,pz,dx,dy,dz))

validDx = None
validDy = None
validDz = None

for i in range(0,len(lines)):
    for j in range(i+1,len(lines)):
        (px1,py1,pz1,dx1,dy1,dz1) = lines[i]
        (px2,py2,pz2,dx2,dy2,dz2) = lines[j]
        
        if dx1 == dx2:
            if validDx is None:
                validDx = validVelocities(px1,px2,dx1)
            else:
                validDx &= validVelocities(px1,px2,dx1)

        if dy1 == dy2:
            if validDy is None:
                validDy = validVelocities(py1,py2,dy1)
            else:
                validDy &= validVelocities(py1,py2,dy1)

        if dz1 == dz2:
            if validDx is None:
                validDz = validVelocities(pz1,pz2,dz1)
            else:
                validDz &= validVelocities(pz1,pz2,dz1)

if len(validDx) != 1 or len(validDy) != 1 or len(validDz) != 1:
    print('This strategy will not work lol')
    print(validDx)
    print(validDy)
    print(validDz)
    exit()

print(validDx)
print(validDy)
print(validDz)

rockDx = validDx.pop()
rockDy = validDy.pop()
rockDz = validDz.pop()

rockX = None
rockY = None
rockZ = None

#if a hailstone has the same dn velocity as the rock I throw, I have to start at the same pn for that axis
for i in range(0,len(lines)):
    (px,py,pz,dx,dy,dz) = lines[i]
    if dx == rockDx:
        rockX = px
    if dy == rockDy:
        rockY = py
    if dz == rockDz:
        rockZ = pz

print(rockX)
print(rockY)
print(rockZ)

#This code only works because I know my Y position exactly. If you knew a different axis, you'd need to
#change the code accordingly. If you had no known starting positions, this plan will not work. This means
#that I don't know how to solve the example problem :D

(px,py,pz,dx,dy,dz) = lines[0]
print(f'hailstone line: y = {py} + {dy}t')
print(f'rock line: y = {rockY} + {rockDy}t')
dyDiff = rockDy-dy
time = (py - rockY) // dyDiff

rockCollisionX = px + (dx * time)
rockCollisionZ = pz + (dz * time)
rockX = rockCollisionX - (rockDx * time)
rockZ = rockCollisionZ - (rockDz * time)
print(rockX + rockY + rockZ)