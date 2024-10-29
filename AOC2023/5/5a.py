file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()


seeds = z.split('\n')[0]
seeds = seeds.split(' ')[1:]
for s in range(0,len(seeds)):
    seeds[s] = int(seeds[s])


mappings = []

for section in z.split('\n\n')[1:]:
    mappings.append([])
    for line in section.split('\n')[1:]:
        dest, src, length = line.split(' ')
        dest = int(dest)
        src = int(src)
        length = int(length)
        mappings[-1].append((dest,src,length))

for mapping in mappings:
    for s in range(0,len(seeds)):
        seed = seeds[s]
        found = False
        for (dest,src,length) in mapping:
            if src <= seed and seed < src+length:
                found = True
                seeds[s] = seed - src + dest
                break
        if not found:
            seeds[s] = seed
    #print(seeds)

print(min(seeds))

