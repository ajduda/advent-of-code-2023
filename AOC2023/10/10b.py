file = 'test.txt'
file = 'input.txt'

LEFT = -1
RIGHT = 1
DOWN = -2
UP    = 2

possible = {}
possible['S'] = {LEFT,RIGHT,DOWN,UP}
possible['.'] = set()
possible['L'] = {RIGHT,UP}
possible['J'] = {LEFT,UP}
possible['7'] = {LEFT,DOWN}
possible['F'] = {RIGHT,DOWN}
possible['|'] = {DOWN,UP}
possible['-'] = {LEFT,RIGHT}
possible['W'] = set()

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
    grid.append(['W'])
    for c in line:
        if c == 'I' or c == 'O':
            grid[-1].append('.')
        else:
            grid[-1].append(c)
        x += 1
    grid[-1].append('W')
    y += 1

grid.append([])
for i in range(0,len(grid[1])):
    grid[0].append('W')
    grid[-1].append('W')


biggerGrid = []
for y in range(0,len(grid)):
    biggerGrid.append([])
    biggerGrid.append([])
    for x in range(0,len(grid[y])):
        match grid[y][x]:
            case 'W':
                biggerGrid[-2].append('W')
                biggerGrid[-2].append('W')
                biggerGrid[-1].append('W')
                biggerGrid[-1].append('W')
            case '|':
                biggerGrid[-2].append('|')
                biggerGrid[-2].append('.')
                biggerGrid[-1].append('|')
                biggerGrid[-1].append('.')
            case '-':
                biggerGrid[-2].append('-')
                biggerGrid[-2].append('-')
                biggerGrid[-1].append('.')
                biggerGrid[-1].append('.')
            case 'L':
                biggerGrid[-2].append('L')
                biggerGrid[-2].append('-')
                biggerGrid[-1].append('.')
                biggerGrid[-1].append('.')
            case 'J':
                biggerGrid[-2].append('J')
                biggerGrid[-2].append('.')
                biggerGrid[-1].append('.')
                biggerGrid[-1].append('.')
            case '7':
                biggerGrid[-2].append('7')
                biggerGrid[-2].append('.')
                biggerGrid[-1].append('|')
                biggerGrid[-1].append('.')
            case 'F':
                biggerGrid[-2].append('F')
                biggerGrid[-2].append('-')
                biggerGrid[-1].append('|')
                biggerGrid[-1].append('.')
            case '.':
                biggerGrid[-2].append('.')
                biggerGrid[-2].append('.')
                biggerGrid[-1].append('.')
                biggerGrid[-1].append('.')
            case 'S':
                biggerGrid[-2].append('S')
                biggerGrid[-2].append('-')
                biggerGrid[-1].append('|')
                biggerGrid[-1].append('.')
            case _:
                print('error')
                exit()

oldGrid = grid
grid = biggerGrid


# debugging grid printing to ensure it blows up properly
# for y in range(0,len(grid)):
#     s = ''
#     for x in range(0,len(grid[y])):
#         s += grid[y][x]
#     print(s)

for y in range(0,len(grid)):
    for x in range(0,len(grid[y])):
        if grid[y][x] == 'S':
            start = (y,x)

loop = {start}
bfs = {start}

while len(bfs) > 0:
    nextBfs = set()
    for coord in bfs:
        landType = getLandType(grid,coord)
        for direction in possible[landType]:
            nextSpot = translate(coord, direction)
            if nextSpot in loop:
                continue
            nextType = getLandType(grid, nextSpot)
            if direction*-1 in possible[nextType]:
                nextBfs.add(nextSpot)
    bfs = nextBfs
    for coord in bfs:
        loop.add(coord)



inside = set()
outside = set()

for y in range(1,len(grid)-1):
    for x in range(1,len(grid[y])-1):
        coord = (y,x)
        if coord in inside or coord in outside or coord in loop:
            continue
        inLoop = True
        region = {coord}
        regionExpanded = set()
        while len(region) > 0:
            land = region.pop()
            regionExpanded.add(land)
            landType = getLandType(grid,land)
            if landType == 'W':
                inLoop = False
                continue
            if land in loop:
                continue
            for direction in possible['S']:
                if translate(land,direction) not in regionExpanded and translate(land,direction) not in loop:
                    region.add(translate(land,direction))
        if inLoop:
            for coord in regionExpanded:
                inside.add(coord)
        else:
            for coord in regionExpanded:
                outside.add(coord)
        #print(f'finished {y},{x}')
        #print(f'loop: {loop}')
        #print(f'outside: {outside}')
        #print(f'inside: {inside}')

#flood fill mostly works but there's weird cases to consider. But the remaining inside regions are all that's left

ans = 0

for y in range(0,len(grid),2):
    for x in range(0,len(grid[y]),2):
        if (y,x) in inside:
            ans += 1

# # debugging statements
# for y in range(0,len(grid)):
#     s = ''
#     for x in range(0,len(grid[y])):
#         if (y,x) in loop:
#             s += grid[y][x]
#         elif (y,x) in outside:
#             s += 'O'
#         elif (y,x) in inside:
#             s += 'I'
#         elif grid[y][x] == 'W':
#             s += 'O'
#         else:
#             print('I found something weird!')
#             exit()
#     print(s)

print(ans)
