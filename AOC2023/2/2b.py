file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    #color maxes
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
                if number > b:
                    b = number
            case 'g':
                if number > g:
                    g = number
            case 'r':
                if number > r:
                    r = number
            case _:
                print(f'error, {color} was found')
        i += 2
    ans += (r*g*b)
print()
print(ans)