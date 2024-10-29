file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

directions, lines = z.split('\n\n')

mapping = {}

for line in lines.split('\n'):
    src, _, left, right = line.split(' ')
    left = left[1:-1]
    right = right[:-1]
    mapping[src] = (left, right)

location = 'AAA'
steps = 0

while location != 'ZZZ':
    d = directions[steps%len(directions)]
    match d:
        case 'L':
            location = mapping[location][0]
        case 'R':
            location = mapping[location][1]
        case _:
            print('I found a bad direction')
    steps += 1

print(steps)