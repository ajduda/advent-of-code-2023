file = 'test.txt'
file = 'input.txt'

def printGrid(grid):
    for line in grid:
        s = ''
        for c in line:
            s += c
        print(line)

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

grid = []
for line in z.split('\n'):
    grid.append([])
    for c in line:
        grid[-1].append(c)

#printGrid(grid)

print()
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

lineScore = len(grid)

for line in grid:
    for c in line:
        if c == 'O':
            ans += lineScore
    lineScore -= 1


print(ans)