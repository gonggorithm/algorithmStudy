n=int(input())

tree = [[] for i in range (n+1)]

for i in range (n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0]*(n+1)
arr=[]

def dfs(s):
    for i in tree[s]:
        if visited[i]==0:
            visited[i]=s
            dfs(i)

dfs(1)
for x in range (2,n+1):
    print(visited[x])