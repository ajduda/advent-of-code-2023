file = 'test.txt'
file = 'input.txt'

def hash(s):
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value %= 256
    return value

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    for s in line.split(','):
        ans += hash(s)

print(ans)