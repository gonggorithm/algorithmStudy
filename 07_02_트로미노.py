n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_num = 0

# 1) 3칸 블럭 탐색

# 1-1) 가로 3칸 블럭 탐색
r_max = 0
for i in range(n):
    for j in range(m-2):
        r_sum = grid[i][j]+grid[i][j+1]+grid[i][j+2]
        r_max = max(r_sum,r_max)

# 1-2) 세로 3칸 블럭 탐색
c_max = 0
for i in range(n-2):
    for j in range(m):
        c_sum = grid[i][j]+grid[i+1][j]+grid[i+2][j]
        c_max = max(c_sum,c_max)

# 2) 꺾인 블록 탐색 (4칸 중 한 칸이 빈 블록이라 생각하기)
s_max = 0
for i in range(n-1):
    for j in range(m-1):
        s_sum_1 = grid[i][j+1]+grid[i+1][j]+grid[i+1][j+1]
        s_sum_2 = grid[i][j]+grid[i+1][j]+grid[i+1][j+1]
        s_sum_3 = grid[i][j]+grid[i][j+1]+grid[i+1][j+1]
        s_sum_4 = grid[i][j]+grid[i][j+1]+grid[i+1][j]
        s_max = max(s_max,s_sum_1,s_sum_2,s_sum_3,s_sum_4)

max_num = max(r_max,c_max,s_max)

print(max_num)
