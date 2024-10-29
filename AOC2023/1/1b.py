file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

first = -1

for line in z.split('\n'):
    first = -1
    last = -1
    for i in range(0,len(line)):
        c = line[i]
        if c.isdigit():
            if first == -1:
                first = int(c)
            last = int(c)
        else:
            if i + 5 <= len(line):
                if line[i:i+5] == 'eight':
                    if first == -1:
                        first = 8
                    last = 8
                if line[i:i+5] == 'seven':
                    if first == -1:
                        first = 7
                    last = 7
                if line[i:i+5] == 'three':
                    if first == -1:
                        first = 3
                    last = 3
            if i + 4 <= len(line):
                if line[i:i+4] == 'nine':
                    if first == -1:
                        first = 9
                    last = 9
                if line[i:i+4] == 'five':
                    if first == -1:
                        first = 5
                    last = 5
                if line[i:i+4] == 'four':
                    if first == -1:
                        first = 4
                    last = 4
            if i + 3 <= len(line):
                if line[i:i+3] == 'six':
                    if first == -1:
                        first = 6
                    last = 6
                if line[i:i+3] == 'two':
                    if first == -1:
                        first = 2
                    last = 2
                if line[i:i+3] == 'one':
                    if first == -1:
                        first = 1
                    last = 1

    ans += (10*first) + last
    #print(10*first + last)

print(ans)