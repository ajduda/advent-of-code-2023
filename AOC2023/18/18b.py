file = 'smallTest.txt'
file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

x = 0
y = 0

dug = 0

xDivs = set()
yDivs = set()

verticalLines = set()
horizontalLines = set()

for line in z.split('\n'):
    inst = line.split(' ')[2]
    length = inst[2:-2]
    length = int(length,16)
    d = int(inst[-2])
    match d:
        case 0:  # Right
            xDivs.add(y)
            horizontalLines.add((y,x,y,x+length))
            x += length
        case 1:  # Down
            yDivs.add(x)
            verticalLines.add((y,x,y+length,x))
            y += length
        case 2:  # Left
            xDivs.add(y)
            horizontalLines.add((y,x,y,x-(length)))
            x -= length
        case 3:  # Up
            yDivs.add(x)
            verticalLines.add((y,x,y-(length),x))
            y -= length
        case _:
            print(f'error: direciton was {d}')
            exit()
    #print((y,x))
    dug += length

"""#personal testing: check for intersecting lines to see if shape is a loop or if it crosses itself
for vLine in verticalLines:
    for hLine in horizontalLines:
        a = vLine[1] #x coordinate
        b = hLine[0] #y coordinate
        if hLine[1] < a and a < hLine[3] and vLine[0] < b and b < vLine[2]:
            print('INTERSECTION')
            print(vLine)
            print(hLine)
exit()"""

#Thus begins actual code again
xDivs = list(xDivs)
xDivs.sort()
yDivs = list(yDivs)
yDivs.sort()

blocks = set()  #coordinates of blocks that are in the lava blocks. Any two adjacent blocks will need to add the space later

for i in range(0,len(yDivs)-1):
    for j in range(0,len(xDivs)-1):
        x = (yDivs[i] + yDivs[i+1]) // 2  # halfway between 2 y lines
        y = (xDivs[j] + xDivs[j+1]) // 2  # halfway between 2 x lines
        #print(f'checking {(y,x)}')
        seenLines = 0
        #Cast rays from the center point of each div region to the right, if we count an odd number of lines intersecting, we're in the shape
        for line in verticalLines:
            #print((y,x))
            #print(line)
            (y1,x1,y2,x2) = line
            if x1 > x:
                if (y1 < y and y < y2) or (y2 < y and y < y1):
                    seenLines += 1
        if seenLines % 2 == 1:
            #add this region to the sum. don't count the lines, they will be added last
            yLen = yDivs[i+1] - yDivs[i] - 1
            #print(yLen)
            xLen = xDivs[j+1] - xDivs[j] - 1
            #print(xLen)
            dug += (yLen * xLen)
            # Missing the spaces between blocks of lava that aren't edge, add once we know what blocks are in
            blocks.add((i,j))

            
for i in range(0,len(yDivs)-1):
    for j in range(0,len(xDivs)-1):
        if (i,j) not in blocks:
            continue
        if (i+1,j) in blocks:
            #ydivs[i] and ydivs[i+1] were both blocks, add that horizontal line between them
            dug += xDivs[j+1]-xDivs[j]-1
        if (i,j+1) in blocks:
            #xdivs[j] and xdivs[j+1] were both in blocks, add the vertical line between them
            dug += yDivs[i+1]-yDivs[i]-1
        if (i+1,j) in blocks and (i,j+1) in blocks and (i+1,j+1) in blocks:
            #I'll forever rue the inner block corner case
            dug += 1

print(dug)