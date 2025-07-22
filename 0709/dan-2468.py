from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def link(start_x, start_y):
    global visited
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    neighbor = deque()
    neighbor.append((start_x, start_y))
    visited[start_x][start_y] = True

    while neighbor:
        x, y = neighbor.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and visited[nx][ny] == False and grid[nx][ny] != 0:
                neighbor.append((nx, ny))
                visited[nx][ny] = True

def search():
    global visited, grid
    max_cnt = 0

    for num in range(101):
        tmp = grid
        drop(num)
        visited = [[False] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j] == False and grid[i][j] != 0:
                    link(i, j)
                    cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
        grid = tmp
    return max_cnt

def drop(rain):
    for i in range(n):
        for j in range(n):
            if grid[i][j] <= rain:
                grid[i][j] = 0

print(search())
# for rows in grid:
#     print(*rows)