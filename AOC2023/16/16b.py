file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

RIGHT = 1
LEFT = -1
DOWN = 2
UP = -2

def next(laser):
    (y,x,direction) = laser
    if direction == RIGHT:
        x += 1
    elif direction == LEFT:
        x -= 1
    elif direction == DOWN:
        y += 1
    elif direction == UP:
        y -= 1
    else:
        print('error: direction')
    return (y,x,direction)

def runSimulation(grid,startingLaser):
    energised = set()
    lasers = [startingLaser]
    while len(lasers) > 0:
        laser = lasers.pop()
        #print(f'new laser: {laser}')
        alive = True
        while alive:
            laser = next(laser)
            #print(laser)
            (y,x,direction) = laser
            land = grid[y][x]

            if land == 'x':
                alive = False
                break
            elif land == '.':
                pass
            elif land == '/':
                if direction == UP:
                    direction = RIGHT
                elif direction == RIGHT:
                    direction = UP
                elif direction == DOWN:
                    direction = LEFT
                elif direction == LEFT:
                    direction = DOWN
                else:
                    print(f'ERROR: / direction was {direction}')
                    exit()
                laser = (y,x,direction)  # actually assign the direction
            elif land == '\\':
                if direction == UP:
                    direction = LEFT
                elif direction == LEFT:
                    direction = UP
                elif direction == DOWN:
                    direction = RIGHT
                elif direction == RIGHT:
                    direction = DOWN
                else:
                    print(f'ERROR: \\ direction was {direction}')
                    exit()
                laser = (y,x,direction)  # actually assign the direction
            elif land == '|':
                if direction == UP or direction == DOWN:
                    pass
                elif direction == RIGHT or direction == LEFT:
                    alive = False
                    if (y,x) not in energised:
                        lasers.append((y,x,UP))
                        lasers.append((y,x,DOWN))
                else:
                    print(f'ERROR: | direction was {direction}')
                    exit()
            elif land == '-':
                if direction == RIGHT or direction == LEFT:
                    pass
                elif direction == UP or direction == DOWN:
                    alive = False
                    if (y,x) not in energised:
                        lasers.append((y,x,LEFT))
                        lasers.append((y,x,RIGHT))
                else:
                    print(f'ERROR: - direction was {direction}')
                    exit()
            else:
                print(f'ERROR: Land was {land}')
                exit()
            energised.add((y,x))
    return len(energised)


grid = []
grid.append([])

for line in z.split('\n'):
    grid.append(['x'])
    for c in line:
        grid[-1].append(c)
    grid[-1].append('x')

grid.append([])
for i in range(0,len(grid[1])):
    grid[0].append('x')
    grid[-1].append('x')


maximum = -1
for x in range(1,len(grid[0])-1):
    n = runSimulation(grid,(0,x,DOWN))
    if n > maximum:
        maximum = n
    n = runSimulation(grid,(len(grid)-1,x,UP))
    if n > maximum:
        maximum = n

for y in range(1,len(grid)-1):
    n = runSimulation(grid,(y,0,RIGHT))
    if n > maximum:
        maximum = n
    n = runSimulation(grid,(y,len(grid[y])-1,LEFT))
    if n > maximum:
        maximum = n



print(maximum)