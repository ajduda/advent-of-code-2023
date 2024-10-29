#I stole this :/
def lcm(a, b):
  t = a % b
  if t == 0: return a
  return a * lcm(b, t) // t

#This one doesn't even pretend to be testable with the test input
file = 'input.txt'

TESTINGCYCLES = 50000

printArrow = {}
printArrow[True] = '-low->'
printArrow[False] = '-high->'




with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

nodes = {}
types = {}

for line in z.split('\n'):
    l,r = line.split(' -> ')
    k = l[1:]
    nodes[k] = []
    types[k] = l[0]
    for item in r.split(', '):
        nodes[k].append(item)

#Set up our structures
flipFlops = {}
conjunction = {}
for k in types:
    if types[k] == '%':
        flipFlops[k] = True  # flip flops start low

for k in types:
    if types[k] == '&':
        conjunction[k] = {}
        for key in nodes:
            if k not in nodes[key]:
                continue
            conjunction[k][key] = True  # it remembers a low pulse for each input


lows = 0
highs = 0
buttonPress = []

for elem in nodes['roadcaster']:  # I truncate the b on accident when parsing :D
    buttonPress.append((elem,True,'roadcaster'))  # True = low pulse, False = high palse

buttonPresses = 0

patterns = {}
patterns['dl'] = []
patterns['fr'] = []
patterns['bt'] = []
patterns['rv'] = []

while buttonPresses < TESTINGCYCLES:
    buttonPresses += 1
    queue = buttonPress.copy()
    while len(queue) > 0:
        (node,signal,fromWhichNode) = queue.pop(0)

        if node == 'rx' and signal == True:
            print(buttonPresses)
            exit()

        if node not in nodes:
            continue

        match types[node]:
            case '%':  # flip flops
                if signal:  # low pulses only do stuff for FF's
                    ffState = not flipFlops[node]
                    flipFlops[node] = ffState
                    for elem in nodes[node]:
                        #print(f'{node} {printArrow[ffState]} {elem}')
                        queue.append((elem,ffState,node))
            case '&':
                #only %rs outputs to rx
                conjunction[node][fromWhichNode] = signal
                if node == 'rs' and not signal:  # we are part of the win condition
                    print(f'Iteration {buttonPresses}, {fromWhichNode} was just high, outputs are {conjunction[node]}')
                    patterns[fromWhichNode].append(buttonPresses)
                outputLow = True
                #print(f'{node} : {conjunction[node]}')
                for key in conjunction[node]:
                    if conjunction[node][key]:
                        outputLow = False
                        break
                for elem in nodes[node]:
                    #print(f'{node} {printArrow[outputLow]} {elem}')
                    queue.append((elem,outputLow,node))

LCM = 1

for k in patterns:
    print(k)
    print(patterns[k])
    diff = []
    for i in range(0,len(patterns[k])-1):
        diff.append(patterns[k][i+1]-patterns[k][i])
    print(diff)
    LCM = lcm(LCM,diff[1])

print(LCM)
