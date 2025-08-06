#타뷸레이션
n=int(input())

dp=[[0]*10 for _ in range(n+1)]

for i in range(1,10):
  dp[1][i]=1

for i in range(2, n+1):
  for j in range(10):
    if j==0:
      dp[i][j]=dp[i-1][1]
    elif j==9:
      dp[i][j]=dp[i-1][8]
    else:
      dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]

result=0
for i in range(10):
  result+=dp[n][i]

result=result%1000000000
print(result)

#메모이제이션
import sys
sys.setrecursionlimit(10000)

n=int(input())

dp=[[-1]*10 for _ in range(n+1)]

def stair(num,last):
  if num==1:
    if last==0:
      return 0
    return 1
  
  if dp[num][last] != -1:
    return dp[num][last]
  
  dp[num][last]=0

  if last==0:
    dp[num][last]=stair(num-1, 1)
  elif last==9:
    dp[num][last]=stair(num-1, 8)
  else:
    dp[num][last]=stair(num-1, last-1) + stair(num-1, last+1)

  return dp[num][last]

answer=0
for i in range(10):
  answer+=stair(n,i)

answer=answer%1000000000
print(answer)