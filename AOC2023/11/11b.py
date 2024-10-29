(file,EXPAND_VAL) = ('test.txt',100)
(file,EXPAND_VAL) = ('input.txt',1000000)

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

galaxies = []

y = 0
for line in z.split('\n'):
    x = 0
    for c in line:
        if c == '#':
            galaxies.append((y,x))
        x += 1
    y += 1

columnsWithoutGalaxies = set()
rowsWithoutGalaxies = set()

for i in range(0,x):
    columnsWithoutGalaxies.add(i)

for i in range(0,y):
    rowsWithoutGalaxies.add(i)

for (y,x) in galaxies:
    if y in rowsWithoutGalaxies:
        rowsWithoutGalaxies.remove(y)
    if x in columnsWithoutGalaxies:
        columnsWithoutGalaxies.remove(x)


for i in range(0,len(galaxies)):
    for j in range(i+1,len(galaxies)):
        y1,x1 = galaxies[i]
        y2,x2 = galaxies[j]
        ydiff = 0
        xdiff = 0
        for row in rowsWithoutGalaxies:
            if (y1 < row and row < y2) or (y2 < row and row < y1):
                ydiff += EXPAND_VAL-1
        for col in columnsWithoutGalaxies:
            if (x1 < col and col < x2) or (x2 < col and col < x1):
                xdiff += EXPAND_VAL-1
        ans += abs(x2-x1) + xdiff
        ans += abs(y2-y1) + ydiff

print(ans)