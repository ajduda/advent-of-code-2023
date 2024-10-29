file = 'test.txt'
file = 'input.txt'

grid = [[]]

ans = 0

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
        if grid[y][x] == '*':
            neighbors = 0
            annoyingCase = False
            #above cases
            if grid[y-1][x-1].isdigit() and gird[y-1][x+1].isdigit() and not grid[y-1][x].isdigit():
                neighbors += 2
                annoyingCase = True
            elif grid[y-1][x].isdigit():
                neighbors += 1
            elif gird[y-1][x-1].isdigit()
                neighbors += 1
            elif grid[y-1][x+1].isdigit()
                neighbors += 1

            #below cases
            if grid[y+1][x-1].isdigit() and gird[y+1][x+1].isdigit() and not grid[y+1][x].isdigit():
                neighbors += 2
                annoyingCase = True
            elif grid[y+1][x].isdigit():
                neighbors += 1
            elif gird[y+1][x-1].isdigit()
                neighbors += 1
            elif grid[y+1][x+1].isdigit()
                neighbors += 1

            #side cases
            if grid[y][x-1].isdigit():
                neighbors += 1
            if grid[y][x+1].isdigit():
                neighbors += 1

            if neighbors == 2:
                if not annoyingCase:
                    #It was at this line I stopped because I didn't want to handle even the not annoying case lol


print(ans)