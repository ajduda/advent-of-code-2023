file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

def minLength(group):
    if len(group) == 0:
        return 0
    return sum(group) + len(group) - 1

def possible(arr,group):
    #print(f'Possible called with arr {arr} and group {group}')
    left = group[0]
    totalPossible = 0
    if len(group) == 1:  #special case the 1 case at the start. Repeat code but easiest for me to implement
        #print('Special Case')
        for i in range(0, len(arr)-left+1):
            if i > 0 and arr[i-1] == '#':
                continue
            if i + left < len(arr) and arr[i+left] == '#':
                continue
            valid = True
            for j in range(i,i+left):
                if arr[j] == '.':
                    valid = False
                    break
            if valid: #confirm there are no #'s after the "last" #
                for j in range(i+left,len(arr)):
                    if arr[j] == '#':
                        valid = False
                        break
            if valid: #confirm there are no #'s before the "first" #
                for j in range(0,i):
                    if arr[j] == '#':
                        valid = False
                        break
            if valid:
                totalPossible += 1
        #print(f'special case returned {totalPossible}')
        return totalPossible

    #print('General Case')
    for i in range(0,len(arr)-minLength(group)+1):
        if i > 0 and arr[i-1] == '#':
            continue
        if arr[i+left] == '#':
            continue
        valid = True
        for j in range(i,i+left):
            if arr[j] == '.':
                valid = False
                break
        if valid: #confirm there are no #'s before the "first" #
            for j in range(0,i):
                if arr[j] == '#':
                    valid = False
                    break
            if valid:
                index = i + left + 1 #start 2 after the last # ends for this position
                totalPossible += possible(arr[index:],group[1:])
    return totalPossible



ans = 0

lineNum = -1

for line in z.split('\n'):
    lineNum += 1
    if lineNum % 50 == 0:
        print(f'REACHED LINENUM {lineNum}')
    print(f'starting line: {line}')
    left, right = line.split(' ')
    arr = []
    for c in left:
        arr.append(c)
    group = []
    for n in right.split(','):
        group.append(int(n))

    p =  possible(arr,group)
    print(p)
    ans += p


print(ans)