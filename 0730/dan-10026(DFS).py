import sys
sys.setrecursionlimit(100000)

n = int(input())
grid = [list(input()) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
cnt = 0
RG_cnt = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 일반
def dfs(x, y):
    visited[x][y] = True
    
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == grid[x][y]:
            dfs(nx, ny)

# 적녹색약
def RG_dfs(x, y):
    visited[x][y] = True
    
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx, ny) and not visited[nx][ny]:
            if grid[x][y] in ["R", "G"]:
                if grid[nx][ny] in ["R", "G"]:
                    RG_dfs(nx, ny)
            else:
                if grid[nx][ny] == grid[x][y]:
                    RG_dfs(nx, ny)

# 일반
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1

# 적녹색약

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            RG_dfs(i, j)
            RG_cnt += 1

print(cnt, RG_cnt)