file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for block in z.split('\n\n'):
    lines = []
    for line in block.split('\n'):
        lines.append(line)
    #check rows
    for i in range(0,len(lines)-1):
        lowLine = i
        highLine = i+1
        valid = True
        while lowLine >= 0 and highLine < len(lines):
            if lines[lowLine] != lines[highLine]:
                valid = False
                break
            lowLine -= 1
            highLine += 1
        if valid:
            ans += (i+1) * 100
            break
    if valid:
        continue
    cols = []
    for x in range(0,len(lines[0])):
        cols.append('')
        for y in range(0,len(lines)):
            cols[-1] += lines[y][x]
    #check columns
    for i in range(0,len(cols)-1):
        lowLine = i
        highLine = i+1
        valid = True
        while lowLine >= 0 and highLine < len(cols):
            if cols[lowLine] != cols[highLine]:
                valid = False
                break
            lowLine -= 1
            highLine += 1
        if valid:
            ans += i + 1
            break

print(ans)