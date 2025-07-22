n,m=map(int, input().split())

def permute_trans(n: int, m: int) -> list[list[int]]:
  results=[]

  def dfs(path: list[int], elements: list[int]):
    if len(path) == m:
      print(' '.join(map(str, path)))
      results.append(path[:])
      return

    for i in range(len(elements)):
      next_path = path + [elements[i]]
      next_elements = elements[:i] + elements[i+1:]
      dfs(next_path, next_elements)

  nums=list(range(1, n+1))
  dfs([], nums)
  return results    

permute_trans(n,m)