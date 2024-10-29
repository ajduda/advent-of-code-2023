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
    for c in line:
        if c.isdigit():
            if first == -1:
                first = int(c)
            last = int(c)
    ans += (10*first) + last

print(ans)