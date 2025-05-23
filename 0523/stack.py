N = int(input())
command = [] # push,pop,size,empty,top을 저장하는 리스트
value = []   # 'push n'일 때 n을 저장하는 리스트

#n개 줄의 명령어를 우선 저장
for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0) # index를 맞춰야하니까

# 스택 자료구조를 구현
class Stack:
    def __init__(self):
        self.items = []
                
    def push(self, item):
        self.items.append(item)
                
    def pop(self):
        if self.empty(): # 문제에 불가능한 명령은 주어지지 않는다 했으니 사실 필요없는 조건이긴 함.
            return -1
        return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        if not self.items:
            return 1
        return 0

    def top(self):
        if self.empty(): # 마찬가지로 문제 영역 밖. 근데 사실 이런 경우 raise Exception해야 함.
            return -1
        return self.items[-1]

# 클래스를 이용해 객체 생성
stack = Stack()

for i in range(N):
    if command[i] == "push":
        stack.push(value[i])
    elif command[i] == "pop":
        print(stack.pop())
    elif command[i] == "size":
        print(stack.size())
    elif command[i] == "empty":
        if stack.empty() == 1:
            print(1)
        else:
            print(0)
    elif command[i] == "top":
            print(stack.top())