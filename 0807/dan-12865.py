n, k = map(int, input().split())

w = []
v = []
for _ in range(n):
    w_input, v_input = map(int, input().split())
    w.append(w_input)
    v.append(v_input)

dp = [[0 for _ in range(n)]for _ in range(k+1)]

for i in range(k+1):
    for j in range(n):
        if j == 0:
            if w[j] <= i:
                dp[i][0] = v[j]
            else:
                dp[i][0] = 0
        else:
            if w[j] <= i:
                dp[i][j] = max(dp[i][j-1], dp[i-w[j]][j-1]+v[j])
            else:
                dp[i][j] = dp[i][j-1]

print(dp[k][n-1])

'''
1차원 dp
dp = [0] * (k + 1)

for _ in range(n):
    w, v = map(int, input().split())
    for j in range(k, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)
'''