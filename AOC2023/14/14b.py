file = 'test.txt'
file = 'input.txt'

CYCLES = 1000000000
BREAKPOINT = 500  # Hopefully a value that is far enough in to find a steady state

def printGrid(grid):
    for line in grid:
        s = ''
        for c in line:
            s += str(c)
        print(s)
    print()

def spinCycle(grid):
    #printGrid(grid)
    #north
    for i in range(1,len(grid)):
        for j in range(0,len(grid[i])):
            if grid[i][j] == 'O':
                y = i
                while grid[y-1][j] == '.':
                    grid[y-1][j] = 'O'
                    grid[y][j] = '.'
                    y -= 1
                    if y == 0:
                        break
    #printGrid(grid)
    #west
    for i in range(0,len(grid)):
        for j in range(1,len(grid[i])):
            if grid[i][j] == 'O':
                x = j
                while grid[i][x-1] == '.':
                    grid[i][x-1] = 'O'
                    grid[i][x] = '.'
                    x -= 1
                    if x == 0:
                        break
    #printGrid(grid)
    #south
    for i in range(len(grid)-2,-1,-1):
        for j in range(0,len(grid[i])):
            if grid[i][j] == 'O': 
                y = i
                while grid[y+1][j] == '.':
                        grid[y+1][j] = 'O'
                        grid[y][j] = '.'
                        y += 1
                        if y == len(grid) - 1:
                            break
    #printGrid(grid)
    #east
    for i in range(0,len(grid)):
        for j in range(len(grid[i])-2,-1,-1):
            if grid[i][j] == 'O':
                x = j
                while grid[i][x+1] == '.':
                    grid[i][x+1] = 'O'
                    grid[i][x] = '.'
                    x += 1
                    if x == len(grid[i]) - 1:
                        break

    #printGrid(grid)

def identical2DGrids(gridA,gridB):
    for i in range(0,len(gridA)):
        for j in range(0,len(gridA[0])):
            if gridA[i][j] != gridB[i][j]:
                return False
    return True


with open(file) as inp:
    z = inp.read()
    z = z.strip()



grid = []
for line in z.split('\n'):
    grid.append([])
    for c in line:
        grid[-1].append(c)

print(f'Starting {BREAKPOINT} cycles')
for i in range(0,BREAKPOINT):
    spinCycle(grid)
print('cycles concluded')

gridSnapshot = []
for line in grid:
    gridSnapshot.append([])
    for elem in line:
        gridSnapshot[-1].append(elem)

period = 1
spinCycle(grid)
while not identical2DGrids(grid,gridSnapshot):
    spinCycle(grid)
    period += 1

print(f'Found a period f {period}')

currentCycles = BREAKPOINT + period
cyclesLeft = CYCLES - currentCycles
cyclesLeft %= period

for i in range(0,cyclesLeft):
    spinCycle(grid)


#score cacluation
lineScore = len(grid)

ans = 0

for line in grid:
    for c in line:
        if c == 'O':
            ans += lineScore
    lineScore -= 1


print(ans)