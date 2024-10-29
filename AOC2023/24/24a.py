file = 'test.txt'
file = 'input.txt'

LOWER = 7
UPPER = 27

LOWER = 200000000000000
UPPER = 400000000000000


lines = []

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    px,py,pz,_,dx,dy,dz = line.split(' ')
    px = int(px[:-1])
    py = int(py[:-1])
    pz = int(pz)
    dx = int(dx[:-1])
    dy = int(dy[:-1])
    dz = int(dz)

    #reminder: point slope form: y - y1 = m(x - x1), or y = m(x-x1) + y1
    # to convert to slope intercept form, y = m(x-x1) + y1 ,y = mx - mx1+y1
    m = dy/dx
    b = py-(m*px)
    lines.append((px,py,dx,dy,m,b))


for i in range(0,len(lines)):
    for j in range(i+1,len(lines)):
        px1,py1,dx1,dy1,m1,b1 = lines[i]
        px2,py2,dx2,dy2,m2,b2 = lines[j]
        print(f'line {i+1}: y = {m1}x + {b1}')
        print(f'line {j+1}: y = {m2}x + {b2}')
        if m1 == m2:  # parallel line or same line
            if (b1 == b2):  # same line
                print('SAME LINE CASE, COME HANDLE THIS LOL')
                print(lines[i])
                print(lines[j])
                print((i,j))
                exit()
            print('these lines are parallel')
        else:  # intersecting line
            #m1x + b1 = m2x + b2
            #m1x-m2x = b2 - b1
            #x = (b2-b1)/(m1-m2)
            x = (b2-b1)/(m1-m2)
            y = m1*x + b1
            print(f'intersection at ({x},{y})')
            if LOWER <= x and x <= UPPER and LOWER <= y and y <= UPPER:
                if (x < px1 and dx1 > 0) or (x > px1 and dx1 < 0):
                    print('in the past for line 1')
                elif (x < px2 and dx2 > 0) or (x > px2 and dx2 < 0):
                    print('in the past for line 2')
                else:
                    ans += 1
                    print('valid intersection')
            else:
                print('intersects out of bounds')



print(ans)