file,STEPCOUNT = 'test.txt',10
file,STEPCOUNT = 'input.txt',300000

#I stole this :/
def lcm(a, b):
  t = a % b
  if t == 0: return a
  return a * lcm(b, t) // t



with open(file) as inp:
    z = inp.read()
    z = z.strip()


ans = 0

directions, lines = z.split('\n\n')

mapping = {}

locations = []

for line in lines.split('\n'):
    src, _, left, right = line.split(' ')
    left = left[1:-1]
    right = right[:-1]
    mapping[src] = (left, right)
    if src[2] == 'A':
        locations.append(src)

print(locations)

steps = 0

successes = {}

while steps < STEPCOUNT:
    d = directions[steps%len(directions)]
    steps += 1
    for i in range(0,len(locations)):
        location = locations[i]
        match d:
            case 'L':
                locations[i] = mapping[location][0]
            case 'R':
                locations[i] = mapping[location][1]
            case _:
                print('I found a bad direction')
        if locations[i][2] == 'Z':
            if i not in successes:
                successes[i] = [steps]
            else:
                successes[i].append(steps)

print(successes)
multiples = []

for arr in successes.values():
    multiples.append(arr[0])

print(multiples)

LCM = 1
for val in multiples:
    LCM = lcm(LCM, val)

print(multiples)
print(LCM)
exit()
# below when I hadn't realized the problem was just LCM
for arr in successes.values():
    i = 0
    while not arr[i+2] - arr[i+1] == arr[i+1] - arr[i]:
        i += 1
    multiples.append((arr[i], arr[i+1] - arr[i]))

print(multiples)


while True:
    #print(multiples)
    multiples.sort()
    if multiples[0][0] == multiples[-1][0]:  # if they all have the same value
        #print(multiples)
        print(multiples[0][0])
        exit()
    multiples[0] = (multiples[0][0] + multiples[0][1], multiples[0][1])