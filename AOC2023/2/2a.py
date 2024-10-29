file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

RED = 12
GREEN = 13
BLUE = 14

game = 0
ans = 0

for line in z.split('\n'):
    game += 1
    r = 0
    g = 0
    b = 0
    words = line.split(' ')
    i = 2
    valid = True
    while i < len(words):
        number = int(words[i])
        color = words[i+1][0]
        match color:
            case 'b':
                if number > BLUE:
                    valid = False
            case 'g':
                if number > GREEN:
                    valid = False
            case 'r':
                if number > RED:
                    valid = False
            case _:
                print(f'error, {color} was found')
        i += 2
    if valid:
        ans += game
        print(game)
print()
print(ans)