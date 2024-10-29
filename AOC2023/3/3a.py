file = 'test.txt'
file = 'input.txt'
file = 'Nick_Input.txt'

notSymbols = {'.','0','1','2','3','4','5','6','7','8','9'}

grid = [[]]

ans = 0

def checkNearby(grid,y,x):
    for i in range(-1,2):
        for j in range(-1,2):
            if grid[y+i][x+j] not in notSymbols:
                return True
    return False

for i in range(0,200):
    grid[-1].append('.')

for line in open(file):
    grid.append(['.','.'])
    for c in line:
        if c == '\n':
            continue
        grid[-1].append(c)
    grid[-1].append('.')
    grid[-1].append('.')
        
grid.append([])
for i in range(0,200):
    grid[-1].append('.')

for y in range(0, len(grid)):
    #print(y)
    for x in range(0, len(grid[y])):
        if grid[y][x].isdigit():
            hasAdjacentSymbol = False
            s = grid[y][x]
            grid[y][x] = '.'
            index = x+1
            hasAdjacentSymbol |= checkNearby(grid,y,x)
            while grid[y][index].isdigit():
                s += grid[y][index]
                grid[y][index] = '.'
                hasAdjacentSymbol |= checkNearby(grid,y,index) # I swapped this with the next line to get it working. I'm a dignus for thinking it would work before
                index += 1
            n = int(s)
            if hasAdjacentSymbol:
                ans += n
            # else:
            #     print(s)
          
# for line in grid:
#     s = ""
#     for c in line:
#         s += c
#     print(s)

print(ans)