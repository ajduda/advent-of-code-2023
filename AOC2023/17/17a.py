file = 'test.txt'
file = 'input.txt'

VERTICAL = True
HORIZONTAL = False

with open(file) as inp:
    z = inp.read()
    z = z.strip()

grid = []

for line in z.split('\n'):
    grid.append([])
    for c in line:
        grid[-1].append(int(c))

finalX = len(grid[0])-1
finalY = len(grid)-1

visited = {}  
seen = {(0,0,True):0,(0,0,False):0} 

while True:
    minKey = None
    minVal = None
    for k,v in seen.items():  #I wish I knew a better way of getting the lowest cost item but I need indexing on coordintes
        if minKey is None or v < minVal:
            minKey = k
            minVal = v
    visited[minKey] = minVal
    seen.pop(minKey)
    cost = minVal
    (y,x,d) = minKey
    if y == finalY and x == finalX:
        print(cost)
        exit()
    #This below section is very code repeaty and I didn't notice until I was almost done, oops. This could have been cleaner
    if d: #vertical direction, expand horizontally
        #Add left elements to seen
        i = 1
        leftSum = cost
        while i <= 3 and x-i >= 0:
            leftSum += grid[y][x-i]
            coord = (y,x-i,False)
            if coord in visited:
                pass
            elif coord not in seen:
                seen[coord] = leftSum
            else:
                if leftSum < seen[coord]:
                    seen[coord] = leftSum
            i += 1
        #Add right elements to seen
        rightSum = cost
        i = 1
        while i <= 3 and x+i < len(grid[0]):
            rightSum += grid[y][x+i]
            coord = (y,x+i,False)
            if coord in visited:
                pass
            elif coord not in seen:
                seen[coord] = rightSum
            else:
                if rightSum < seen[coord]:
                    seen[coord] = rightSum
            i += 1
    else: #horizontal direction, expand vertically
        #Add up elements to seen
        i = 1
        upSum = cost
        while i <= 3 and y-i >= 0:
            upSum += grid[y-i][x]
            coord = (y-i,x,True)
            if coord in visited:
                pass
            elif coord not in seen:
                seen[coord] = upSum
            else:
                if upSum < seen[coord]:
                    seen[coord] = upSum
            i += 1
        #add down elements to seen
        i = 1
        downSum = cost
        while i <= 3 and y+i < len(grid):
            downSum += grid[y+i][x]
            coord = (y+i,x,True)
            if coord in visited:
                pass
            elif coord not in seen:
                seen[coord] = downSum
            else:
                if downSum < seen[coord]:
                    seen[coord] = downSum
            i += 1
