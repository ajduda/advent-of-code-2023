# test input
time = [7,15,30]
distance = [9,40,200]

# my input
time = [34,90,89,86]
distance = [204,1713,1210,1780]

ans = 1

for race in range(0,len(time)):
    winCount = 0
    raceTime = time[race]
    raceDist = distance[race]
    print(f'{raceTime} {raceDist}')
    for t in range(0,raceTime):
        if t*(raceTime - t) > raceDist:
            winCount += 1
    ans *= winCount
    print(winCount)

print(ans)