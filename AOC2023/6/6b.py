# test input
time = 71530
distance = 940200

# my input
time = 34908986
distance = 204171312101780

ans = time + 1  # Fix off by one errors with this one weird trick!

t = 0

while t * time <= distance:
    t += 1
    time -= 1
    ans -= 2

print(ans)