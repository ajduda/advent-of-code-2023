file = 'test.txt'
file = 'input.txt'

LEFT = -1
RIGHT = 1
DOWN = -2
UP =    2

possible = {}
possible['S'] = {LEFT,RIGHT,DOWN,UP}
possible['.'] = {}
possible['L'] = {RIGHT,UP}
possible['J'] = {LEFT,UP}
possible['7'] = {LEFT,DOWN}
possible['F'] = {RIGHT,DOWN}
possible['|'] = {DOWN,UP}
possible['-'] = {LEFT,RIGHT}

def translate(coord, direction):
    (y,x) = coord
    if direction == LEFT:
        return (y,x-1)
    if direction == RIGHT:
        return (y,x+1)
    if direction == UP:
        return (y-1,x)
    if direction == DOWN:
        return (y+1,x)
    print('INVALID DIRECTION GIVEN TO TRANSLATE()')
    exit()

def getLandType(grid, coord):
    (y,x) = coord
    return grid[y][x]

with open(file) as inp:
    z = inp.read()
    z = z.strip()

grid = [[]]
y = 1
for line in z.split('\n'):
    x = 1
    grid.append(['.'])
    for c in line:
        grid[-1].append(c)
        if c == 'S':
            start = (y,x)
        x += 1
    grid[-1].append('.')
    y += 1

grid.append([])
for i in range(0,len(grid[1])):
    grid[0].append('.')
    grid[-1].append('.')

visited = {start}
bfs = {start}
dist = 0

while len(bfs) > 0:
    #print(f'DIST: {dist}')
    #print(f'CURRENT BFS: {bfs}')
    nextBfs = set()
    for coord in bfs:
        landType = getLandType(grid,coord)
        for direction in possible[landType]:
            nextSpot = translate(coord, direction)
            if nextSpot in visited:
                continue
            nextType = getLandType(grid, nextSpot)
            if direction*-1 in possible[nextType]:
                nextBfs.add(nextSpot)
    bfs = nextBfs
    for coord in bfs:
        visited.add(coord)
    dist += 1

print(dist-1)