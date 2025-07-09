n, m = map(int, input().split())
sign = []
for _ in range(n):
    sign.append(list(map(int, input().split())))

sign.sort()

a = 0  # Your 'a' for position
t = 0  # Your 't' for time

while a <= m:
    for e in sign:
        light_position = e[0]
        red_duration = e[1]
        green_duration = e[2]

        if a == light_position:
            cycle_length = red_duration + green_duration
            time_in_cycle = t % cycle_length

            if time_in_cycle < red_duration:
                wait_time = red_duration - time_in_cycle
                t += wait_time
            break

    a += 1
    t += 1

print(t - 1)