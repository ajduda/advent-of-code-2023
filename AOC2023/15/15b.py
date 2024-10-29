file = 'test.txt'
file = 'input.txt'

def hash(s):
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value %= 256
    return value

with open(file) as inp:
    z = inp.read()
    z = z.strip()

boxes = dict()

for i in range(0,256):
    boxes[i] = []

for line in z.split('\n'):
    for s in line.split(','):
        #print(f'processing order {s}')
        if s[-1] == '-': # remove case
            k = s[:-1]
            h = hash(k)
            box = boxes[h]
            for i in range(0,len(box)):
                if box[i][0] == k:
                    #print(f'removed {box[i]} from box number {h}')
                    box.pop(i)
                    break
        elif s[-2] == '=': #assign case
            n = int(s[-1])
            k = s[:-2]
            h = hash(k)
            box = boxes[h]
            found = False
            for i in range(0,len(box)):
                if box[i][0] == k:
                    #print(f'changing {box[i]} to {(box[i][0],n)} in box number {h}')
                    box[i] = (box[i][0],n)
                    found = True
                    break
            if not found:
                box.append((k,n))
                #print(f'added {boxes[h][-1]} to box number {h}')
        else:
            print(f'error value found: {s}')
        #print(boxes)
ans = 0

for box in range(0,256):
    slot = 1
    #if len(boxes[box]) > 0:
        #print(f'{box}: {boxes[box]}')
    for item in boxes[box]:
        ans += item[1] * slot * (box + 1)
        slot += 1

print(ans)