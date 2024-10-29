file = 'test.txt'
file = 'input.txt'

index = {}
index['x'] = 0
index['m'] = 1
index['a'] = 2
index['s'] = 3

rules = {}
parts = []
with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n\n')[0].split('\n'):
    left,right = line.split('{')
    rules[left] = []
    right = right[:-1]
    for elem in right.split(','):
        if ':' in elem:
            l,r = elem.split(':')
            rules[left].append((l,r))
        else:
            rules[left].append(elem)

for line in z.split('\n\n')[1].split('\n'):
    part = []
    temp = line[1:-1]
    for elem in temp.split(','):
        part.append(int(elem[2:]))
    state = 'in'
    while state != 'A' and state != 'R':
        rule = rules[state]
        for (test,dest) in rule[:-1]:
            category = test[0]
            op = test[1]
            number = int(test[2:])
            match op:
                case '>':
                    passes = part[index[category]] > number
                case '<':
                    passes = part[index[category]] < number
                case _:
                    print(f'error: case was {op}')
                    exit()
            if passes:
                state = dest
                break
        else:
            state = rule[-1]
    
    if state == 'A':
        for elem in part:
            ans += elem


print(ans)