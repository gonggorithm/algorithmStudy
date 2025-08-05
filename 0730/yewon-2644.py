from collections import deque

n=int(input())
a,b=map(int, input().split())
m=int(input())

graph=[[] for _ in range(n+1)]

for _ in range(m):
  x,y=map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def relation(graph:list[list[int]], start: int, target: int) -> int:
  visited=[0]*(n+1)
  q=deque()
  q.append(start)
  visited[start]=1

  while q:
    current=q.popleft()
    for i in graph[current]:
      if visited[i] == 0:
        visited[i]=visited[current]+1
        q.append(i)

  if visited[target] == 0:
    return -1
  else:
    return visited[target] -1
  
print(relation(graph,a,b))