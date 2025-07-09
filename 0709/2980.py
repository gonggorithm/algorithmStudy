n, l = map(int, input().split())

a = [tuple(map(int,input().split())) for _ in range(n)]

time = 0    
prev_d = 0

for d, r, g in a:
    time += (d - prev_d)
    if time % (r + g) <= r:
        time += r - (time % (r+g))
    prev_d = d
time += l - prev_d

print(time)
