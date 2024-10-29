file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

def bounds(a,b):
    if a <= b:
        return (a,b+1)
    return (b,a+1)

bricks = []

print('parsing input')

for line in z.split('\n'):
    start,end = line.split('~')
    x1,y1,z1 = start.split(',')
    x2,y2,z2 = end.split(',')
    x1 = int(x1)
    y1 = int(y1)
    z1 = int(z1)
    x2 = int(x2)
    y2 = int(y2)
    z2 = int(z2)
    #storing y first so sorting will get me the lowest y value
    if z2 < z1:
        bricks.append(((z2,x2,zy),(z1,x1,y1)))

    bricks.append(((z1,x1,y1),(z2,x2,y2)))

print('placing blocks')

placedBricks = set()
brickLocations = {}
brickNumber = 0
while len(bricks) > 0:
    bricks.sort()
    #Take the lowest brick in the snapshot. I'm only 95% sure this will work but simulating every brick at once is ow
    ((z1,x1,y1),(z2,x2,y2)) = bricks.pop(0)
    xBounds = bounds(x1,x2)
    yBounds = bounds(y1,y2)
    zBounds = bounds(z1,z2)
    brick = set()
    #This looks horrible but at least 2 bounds will not iterate more than once. This is just a lazy way to cover all cases
    for x in range(xBounds[0],xBounds[1]):
        for y in range(yBounds[0],yBounds[1]):
            for z in range(zBounds[0],zBounds[1]):
                brick.add((z,x,y))  # keeping the z,x,y (or h,x,y depending on how i'm thinking about it)

    falling = True
    while falling:
        nextBrick = set()
        for (z,x,y) in brick:
            if z == 1 or (z-1,x,y) in placedBricks:
                falling = False
                break
            nextBrick.add((z-1,x,y))
        if falling:
            brick = nextBrick

    #register this as placed
    brickLocations[brickNumber] = set()
    for coord in brick:
        placedBricks.add(coord)
        brickLocations[brickNumber].add(coord)
    brickNumber += 1

supportedBy = {}
supporting  = {}

print('building support dictionaries')
# find supporting bricks
for k1 in brickLocations:
    brickCoords = brickLocations[k1]
    coordsToCheck = set()
    for (z,x,y) in brickCoords:
        if (z-1,x,y) in placedBricks:
            coordsToCheck.add((z-1,x,y))

    for coord in coordsToCheck:
        for k2 in brickLocations:
            if k1 == k2:  # You can't support yourself in this problem, silly
                continue
            if coord in brickLocations[k2]:
                if k1 in supportedBy:
                    supportedBy[k1].add(k2)
                else:
                    supportedBy[k1] = {k2}

                if k2 in supporting:
                    supporting[k2].add(k1)
                else:
                    supporting[k2] = {k1}


#some old debug code to see if my stuctures made sense.
#for k in brickLocations:
#    print(f'{k} bricks: {brickLocations[k]}')
#    if k in supporting:
#        print(f'supporting: {supporting[k]}')
#    if k in supportedBy:
#        print(f'supportedBy: {supportedBy[k]}')

ans = 0

print('figuring out the answer')
for k in brickLocations:
    if k not in supporting:
        ans += 1
    else:
        redundant = True
        for otherBrick in supporting[k]:
            if len(supportedBy[otherBrick]) == 1:
                redundant = False
                break
        if redundant:
            ans += 1

print(ans)