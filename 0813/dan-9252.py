A = input()
B = input()

# Please write your code here.
dp = [
    [0 for _ in range(len(B) + 1)]
    for _ in range(len(A) + 1)
]

def initialize():
    for i in range(len(A)+ 1):
        dp[i][0] = 0

    for j in range(0, len(B) + 1):
        dp[0][j] = 0

initialize()

for i in range(1, len(A) + 1):
	for j in range(1, len(B) + 1):
		if A[i-1] == B[j-1]:
			dp[i][j] = dp[i-1][j-1] + 1
		else:
			dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(A)][len(B)])

lcs = []
num = 0
while i > 0 and j > 0:
    if A[i-1] == B[j-1]:
        lcs.append(A[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] >= dp[i][j-1]:
        i -= 1
    else:
        j -= 1
        
lcs.reverse()
for item in lcs:
    print(item, end ="")