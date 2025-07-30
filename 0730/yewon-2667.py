n=int(input())
grid=list(list(input()) for _ in range(n))

def numBlock(grid:list[list[str]]) -> int:
  
  numHouse=[]

  def dfs(i,j):
    if (i<0 or i>=n) or (j<0 or j>=n) or grid[i][j] != '1':
      return 0
    
    grid[i][j]= '0'
    houseCount=1

    houseCount += dfs(i+1,j)
    houseCount += dfs(i-1,j)
    houseCount += dfs(i,j+1)
    houseCount += dfs(i,j-1)

    return houseCount

  blockCount=0
  for i in range(n):
    for j in range(n):
      if grid[i][j] == '1':
        houseCount = dfs(i,j)
        numHouse.append(houseCount)
        blockCount+=1
  
  print(blockCount)
  print('\n'.join(map(str, sorted(numHouse))))

  return blockCount, numHouse

numBlock(grid)

  