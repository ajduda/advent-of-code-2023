# 1b.py was the file that got the original solution. This was me trying to take that idea and make it not so horrible, though it did work

file = 'test.txt'
#file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

first = -1

words = ['one','two','three','four','five','six','seven','eight','nine']

for line in z.split('\n'):
    first = -1
    last = -1
    for i in range(0,len(line)):
        c = line[i]
        if c.isdigit():
            if first == -1:
                first = int(c)
            last = int(c)
        else:
            for j,word in enumerate(words):
#            for j in range(0, len(words)):    # Fake enumerate
#                word = words[j]               # Fake enumerate pt. 2 (final).docx
                l = len(word)
                if i + l <= len(line):
                    if line[i:i+l] == word:
                        if first == -1:
                            first = j + 1
                        last = j + 1

    ans += (10*first) + last
    #print(10*first + last)

print(ans)