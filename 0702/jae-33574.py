n = int(input())
grid = [list(map(int, input().split())) for _ in range(2)]

# 방향: 오른쪽, 아래, 위
dx = [0, 1, -1]
dy = [1, 0, 0]

def dfs(i, j):
    if i == 1 and j == n - 1:
        return True

    grid[i][j] = 0

    for d in range(3):
        ni = i + dx[d]
        nj = j + dy[d]
        if 0 <= ni < 2 and 0 <= nj < n and grid[ni][nj] == 1:
            if dfs(ni, nj):
                return True
    return False

if grid[0][0] == 0:
    print(0)
else:
    print(1 if dfs(0, 0) else 0)
