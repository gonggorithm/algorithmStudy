n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def rhomb_search(grid, x, y, k):
    total = 0
    n = len(grid)
    for dx in range(-k, k + 1):
        dy_range = k - abs(dx)
        for dy in range(-dy_range, dy_range + 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                total += grid[nx][ny]
    return total


max_gold = 0

for k in range(n+1):
    loss = k*k+((k+1)*(k+1))
    for i in range(n):
        for j in range(n):
            gold = rhomb_search(grid,i,j,k)
            r_cost = gold*m
            if r_cost >= loss:
                max_gold = max(max_gold,gold)

print(max_gold)
