file = 'test.txt'
file = 'input.txt'

def fragment(Range, index):
    retA = (Range[0],index-1)
    retB = (index,Range[1])
    return (retA, retB)

def newRange(Range, src, dest):
    (low, high) = Range
    low += dest - src
    high += dest - src
    return (low,high)

with open(file) as inp:
    z = inp.read()
    z = z.strip()


seeds = z.split('\n')[0]
seeds = seeds.split(' ')[1:]
s = 0
temp = []
i = 0
while s < len(seeds):
    temp.append((int(seeds[s]),int(seeds[s])+int(seeds[s+1])))
    s += 2
    i += 1

seedRanges = temp
#print(seedRanges)
mappings = []

for section in z.split('\n\n')[1:]:
    mappings.append([])
    for line in section.split('\n')[1:]:
        dest, src, length = line.split(' ')
        dest = int(dest)
        src = int(src)
        length = int(length)
        mappings[-1].append((src,src+length,dest))
    mappings[-1].sort()

#print(mappings)

for mapping in mappings:
    nextSeedRanges = []
    while len(seedRanges) > 0:
        # print(f"seedRanges: {seedRanges}")
        seedRange = seedRanges.pop(0)
        # print(f'popping seedrange {seedRange}')
        startVal = seedRange[0]
        endVal = seedRange[1]
        foundAMapping = False
        for (start,end,dest) in mapping:
            # print(f'mapping: {mapping}')
            # print(f'start: {start}')
            # print(f'end: {end}')
            # print(f'startVal: {startVal}')
            # print(f'endVal: {endVal}')
            if start >= endVal or end <= startVal: #invalid mapping
                continue
            if start <= startVal and endVal <= end:  #range fits into a mapping
                nextSeedRanges.append(newRange(seedRange, start, dest))     #ready to go to next step
                foundAMapping = True
                #print('CASE A')
                break
            elif start <= startVal and endVal > end: #range doesn't fit, goes too high. send fragments to next iteration
                (rangeA, rangeB) = fragment(seedRange, end)
                seedRanges.append(rangeA)
                seedRanges.append(rangeB)
                foundAMapping = True
                #print('CASE B')
                break
            elif start > startVal and endVal <= end:  # range doesn't fit, starts too low. send fragments to next iteration
                (rangeA, rangeB) = fragment(seedRange, start)
                seedRanges.append(rangeA)
                seedRanges.append(rangeB)
                foundAMapping = True
                #print('CASE C')
                break
            elif start > startVal and endVal < end:  # seed range is outside this range entirely. Fragment into 3 and try again
                (rangeA,rangeT) = fragment(seedrange,start)
                (rangeB,RangeC) = fragment(rangeT, end)
                seedRanges.append(rangeA)
                seedRanges.append(rangeB)
                seedRanges.append(rangeT)
                foundAMapping = True
                #print('CASE D')
                break
        if not foundAMapping:
            nextSeedRanges.append(seedRange)
    seedRanges = nextSeedRanges




seedRanges.sort()
print(seedRanges[0][0])

exit()