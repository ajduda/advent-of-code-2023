file = 'smallTest.txt'
file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

dug = {(0,0)}
x = 0
y = 0

maxX = 0
maxY = 0
minX = 0
minY = 0


for line in z.split('\n'):
    d,n,color = line.split(' ')
    n = int(n)
    match d:
        case 'R':
            dx = 1
            dy = 0
        case 'D':
            dx = 0
            dy = 1
        case 'L':
            dx = -1
            dy = 0
        case 'U':
            dx = 0
            dy = -1
    for i in range(1,n+1):
        x += dx
        y += dy
        dug.add((y,x))

    if x > maxX:
        maxX = x
    if x < minX:
        minX = x
    if y > maxY:
        maxY = y
    if y < minY:
        minY = y

floodFilled = set()
for y in range(minY,maxY+1):
    for x in range(minX,maxX+1):
        if (y,x) in dug or (y,x) in floodFilled:
            continue
        region = {(y,x)}
        regionExpanded = set()
        inArea = True
        while(len(region)) > 0:
            coord = region.pop()
            if coord in dug or coord in regionExpanded:
                continue
            regionExpanded.add(coord)
            (york,xork) = coord
            if york == maxY: #check down
                inArea = False
            else:
                region.add((york+1,xork))
            if york == minY: #check up
                inArea = False
            else:
                region.add((york-1,xork))
            if xork == minX: #check left
                inArea = False
            else:
                region.add((york,xork-1))
            if xork == maxX: #check right
                inArea = False
            else:
                region.add((york,xork+1))
        for coord in regionExpanded:
            if inArea:
                dug.add(coord)
            else:
                floodFilled.add(coord)



#print(minX)
#print(maxX)
#print(minY)
#print(maxY)

#print(dug)
print(len(dug))