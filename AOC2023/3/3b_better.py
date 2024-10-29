file = 'test.txt'
file = 'input.txt'
file = 'Nick_Input.txt'

grid = [[]]

ans = 0

gears = {}

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
            s = grid[y][x]
            grid[y][x] = '.'
            index = x+1
            while grid[y][index].isdigit():
                s += grid[y][index]
                grid[y][index] = '.'
                index += 1
            n = int(s)
            for j in range(y-1,y+2):
                for i in range(x-1,index+1):
                    if grid[j][i] == '*':
                        if (j,i) not in gears:
                            gears[(j,i)] = [n]
                        else:
                            gears[(j,i)].append(n)

print(gears)

#How many gears of any count touch at least one number? Uncomment these lines to find out!
#gearNumbers = [0,0,0,0,0]

for k in gears.keys():
    numbers = gears[k]
    #gearNumbers[len(numbers)] += 1
    if len(numbers) == 2:     
        ans += numbers[0]*numbers[1]

#print(gearNumbers)

print(ans)