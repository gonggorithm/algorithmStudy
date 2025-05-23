#정수명령처리 
from collections import deque
dq=deque()

n = int(input())
cmd = []
num = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        num.append(int(line[1]))
    else:
        num.append(0)

for i in range(n):
    if cmd[i]=="empty":
        print(1 if not dq else 0)
    elif cmd[i]=="push_front":
        dq.appendleft(num[i])
    elif cmd[i]=="push_back":
        dq.append(num[i])
    elif cmd[i]=="pop_front":
        print(dq.popleft())
    elif cmd[i]=="pop_back":
        print(dq.pop())
    elif cmd[i]=="size":
        print(len(dq))
    elif cmd[i]=="front":
        print(dq[0])
    elif cmd[i]=="back":
        print(dq[-1])
    else:
        print("Exception")

#수열조작
from collections import deque

dq=deque()

n = int(input())
for i in range(1,n+1):
    dq.append(i)

for i in range(n-1):
    dq.popleft()
    tmp=dq.popleft()
    dq.append(tmp)

print(dq[-1])
