file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

opposite = dict()
opposite['.'] = '#'
opposite['#'] = '.'

ans = 0

for block in z.split('\n\n'):
    #Part A to get the origional line that needs to be different
    rowAns = -1
    colAns = -1
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
            rowAns = i
            break
    if not valid:
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
                colAns = i
                break


    baseLines = []
    for line in lines:
        baseLines.append(line)
    
    found = False
    #if any code reviewers see york and xork, I'm not sure why I did this either
    for york in range(0,len(baseLines)):
        if found:
            break

        for xork in range(0,len(baseLines[0])):
            if found:
                break

            lines = []
            for n in range(0,len(baseLines)):
                if n == york:
                    lines.append(baseLines[n][:xork] + opposite[baseLines[n][xork]] + baseLines[n][xork+1:])
                else:
                    lines.append(baseLines[n])


            for i in range(0,len(lines)-1):
                if i == rowAns:
                    continue
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
                    found = True
                    print(f'smudge was at ({york},{xork})')
                    break
            if valid:
                continue
            cols = []
            for x in range(0,len(lines[0])):
                cols.append('')
                for y in range(0,len(lines)):
                    cols[-1] += lines[y][x]

            for i in range(0,len(cols)-1):
                if i == colAns:
                    continue
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
                    found = True
                    print(f'smudge was at ({york},{xork})')
                    break

print(ans)