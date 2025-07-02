n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

count = 0

if m == 1:
    count += 2*n
else:
    #가로 확인
    for i in range(n):
        seq = int(m)
        for j in range(n-1):
            if grid[i][j] == grid[i][j+1]:
                seq -= 1
                if seq == 1:
                    count += 1
                    break
            else:
                seq = int(m)

    #세로 확인
    for j in range(n):
        seq = int(m)
        for i in range(n-1):
            if grid[i][j] == grid[i+1][j]:
                seq -= 1
                if seq == 1:
                    count += 1
                    break
            else:
                seq = int(m)

print(count)