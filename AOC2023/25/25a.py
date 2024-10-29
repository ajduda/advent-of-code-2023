file = 'test.txt'
file = 'input.txt'

#random is both the value and the seed here
random = 5  # Oh boy I'm sorta implementing my own RNG, though I've referenced the internet to get the basics again
#values taken from https://stackoverflow.com/a/11946674, in reference to values used by libgc's random function
A = 1103515245
C = 12345
M = 2 ** 31

ITERATIONS = 10000

def rand():
    global random
    random *= A
    random += C
    random %= M
    return random

def pathToTouple(a,b):
    #alphabitize the values to ensure the touple is the same for the same 2 nodes
    l = [a,b]
    l.sort()
    return (l[0],l[1])

def regionSize(nodes,start):
    seen = {start}
    horizon = {start}
    while len(horizon) > 0:
        node = horizon.pop()
        for connectedNode in nodes[node]:
            if connectedNode not in seen:
                seen.add(connectedNode)
                horizon.add(connectedNode)
    return len(seen)


with open(file) as inp:
    z = inp.read()
    z = z.strip()

nodes = {}

for line in z.split('\n'):
    l,r = line.split(': ')
    if l not in nodes:
        nodes[l] = set()
    for node in r.split(' '):
        nodes[l].add(node)
        if node not in nodes:
            nodes[node] = set()
        nodes[node].add(l)

#Something indexable so we can get 2 elements randomly
nodeList = []
for k in nodes:
    nodeList.append(k)

edgeCount = {}

for i in range(0,ITERATIONS):
    if i % 1000 == 0:
        print(f'starting iteration {i}')
    nodeA = nodeList[rand()%len(nodeList)]
    nodeB = nodeList[rand()%len(nodeList)]
    while nodeB == nodeA:  # reroll B on a duplicated pull
        nodeB = nodeList[rand()%len(nodeList)]

    #print((nodeA,nodeB))
    start = nodeA
    end = nodeB
    toSearch = {start}
    seenNodes = {start}
    edgeToNode = {}
    #BFS but expand in waves, basically
    while end not in toSearch:
        nextToSearch = set()
        for node in toSearch:
            for connectedNode in nodes[node]:
                if connectedNode not in seenNodes:
                    seenNodes.add(connectedNode)
                    edgeToNode[connectedNode] = node
                    nextToSearch.add(connectedNode)
        toSearch = nextToSearch
        if len(toSearch) == 0:
            print('we ran out of nodes to find!')
            exit()

    pathNode = end
    while pathNode != start:
        path = pathToTouple(pathNode,edgeToNode[pathNode])
        if path not in edgeCount:
            edgeCount[path] = 1
        else:
            edgeCount[path] += 1
        pathNode = edgeToNode[pathNode]

edgesToSort = []
for k in edgeCount:
    edgesToSort.append((edgeCount[k],k))

edgesToSort.sort()
edgesToSort.reverse()

for i in range(0,3):
    edge = edgesToSort[i][1]
    nodeA,nodeB = edge
    nodes[nodeA].remove(nodeB)
    nodes[nodeB].remove(nodeA)

sizeA = regionSize(nodes,nodeA)
sizeB = regionSize(nodes,nodeB)
print(nodeA,sizeA)
print(nodeB,sizeB)
print(sizeA * sizeB)