def maximize(junctions,start,end,visited):
    if start == end:
        return (True,0)
    myVisited = visited.copy()
    myVisited.add(start)
    maximum = 0
    foundEnd = False
    paths = junctions[start]
    for path in paths:
        if path in myVisited:
            continue
        pathLen = paths[path]
        pathRet = maximize(junctions,path,end,myVisited)
        if pathRet[0]:
            foundEnd = True
            if pathLen + pathRet[1] > maximum:
                maximum = pathLen + pathRet[1]
    return (foundEnd,maximum)


file = 'test.txt'
file = 'input.txt'

ADJACENT = [(-1,0),(1,0),(0,-1),(0,1)]

allowed = {}
allowed[(-1,0)] = '.^<>v'
allowed[(1,0)]  = '.^<>v'
allowed[(0,-1)] = '.^<>v'
allowed[(0,1)]  = '.^<>v'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

#only need top bottom padding, LR is already walls
grid = [[]]

for line in z.split('\n'):
    grid.append([])
    for c in line:
        grid[-1].append(c)

grid.append([])
for i in range(0,len(grid[1])):
    grid[0].append('#')
    grid[-1].append('#')

junctions = {}

for y in range(1,len(grid)-1):
    for x in range(1,len(grid[y])-1):
        if grid[y][x] != '#':
            nonWalls = 0
            for (dy,dx) in ADJACENT:
                if grid[y+dy][x+dx] != '#':
                    nonWalls += 1
            if nonWalls > 2:
                junctions[(y,x)] = {}

#treat the start and end as junctions
for x in range(0,len(grid[0])):
    if grid[1][x] == '.':
        junctions[(1,x)] = {}
        START = (1,x)
    if grid[-2][x] == '.':
        junctions[(len(grid)-2,x)] = {}
        END = (len(grid)-2,x)

for junction in junctions:
    y,x = junction
    for direction in ADJACENT:
        (dy,dx) = direction
        prev = junction
        if grid[y+dy][x+dx] in allowed[direction]:
            tempY = y+dy
            tempX = x+dx
            length = 1
            deadEnd = False
            while (tempY,tempX) not in junctions and not deadEnd:
                for d in ADJACENT:
                    (dyork,dxork) = d  # I love just how stupid of a name this is but it keeps me from mixing them up
                    if (tempY+dyork,tempX+dxork) != prev and grid[tempY+dyork][tempX+dxork] in allowed[d]:
                        prev = (tempY,tempX)
                        tempY += dyork
                        tempX += dxork
                        length += 1
                        break
                else:
                    #we exhausted the path and did not find a junction
                    deadEnd = True
                    break
            if not deadEnd:
                junctions[junction][(tempY,tempX)] = length




print(junctions)
print(len(junctions))


print(maximize(junctions,START,END,set())[1])