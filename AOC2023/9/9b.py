file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    array = [[]]
    for n in line.split(' '):
        array[0].append(int(n))

    allZeroes = False
    while not allZeroes:
        allZeroes = True
        array.append([])
        for i in range(0,len(array[-2])-1):
            array[-1].append(array[-2][i+1] - array[-2][i])
            if array[-2][i+1] - array[-2][i] != 0:
                allZeroes = False
    val = 0
    for i in range(len(array)-1,-1,-1):
        val = array[i][0] - val
    ans += val
    #print(val)

print(ans)