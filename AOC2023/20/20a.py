file = 'test.txt'
file = 'input.txt'

ITERATIONS = 1000
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

for i in range(0,ITERATIONS):
    #print(i)
    queue = buttonPress.copy()
    lows += 1 # buttonpress adds a low
    while len(queue) > 0:
        (node,signal,fromWhichNode) = queue.pop(0)
        
        if signal:
            lows += 1
        else:
            highs += 1

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
                conjunction[node][fromWhichNode] = signal
                outputLow = True
                #print(f'{node} : {conjunction[node]}')
                for key in conjunction[node]:
                    if conjunction[node][key]:
                        outputLow = False
                        break
                for elem in nodes[node]:
                    #print(f'{node} {printArrow[outputLow]} {elem}')
                    queue.append((elem,outputLow,node))
                        
print()
print(lows)
print(highs)
print(lows*highs)