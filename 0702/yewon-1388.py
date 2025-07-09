"""
n = int(input())
map = [list(map(int, input().split())) for _ in range(2)]

result = 3

for c in range(2):
    for r in range(n):
        pointer = map[c][r]
        if c + 1 < 2 and r + 1 < n:
            if c == 0:
                pointer_right = map[c][r + 1]
                pointer_down = map[c + 1][r]
                if pointer_right == 0 and pointer_down == 0:
                    result = 0
            elif c == 1:
                pointer_right = map[c][r + 1]
                pointer_up = map[c - 1][r]
                if pointer_right == 0 and pointer_up == 0:
                    result = 0

if result != 0:
    found_zero = False
    for c in range(2):
        for r in range(n):
            if map[c][r] == 0:
                result = 1
                found_zero = True
                break
        if found_zero:
            break
    else:
        result = 2

print(result)
"""
n = int(input())
grid = [list(map(int, input().split())) for _ in range(2)]

result = 2  # 기본값: 전부 1이면

for c in range(2):
    for r in range(n):
        if grid[c][r] == 0:
            result = 1  # 0이 하나라도 있으면 최소 1

# 가로 또는 세로로 인접한 0이 있으면 → result = 0
for r in range(n):
    if grid[0][r] == 0 and grid[1][r] == 0:  # 세로로 인접한 0
        result = 0
    if r + 1 < n:
        if grid[0][r] == 0 and grid[0][r + 1] == 0:  # 윗줄 가로 0
            result = 0
        if grid[1][r] == 0 and grid[1][r + 1] == 0:  # 아랫줄 가로 0
            result = 0

print(result)
