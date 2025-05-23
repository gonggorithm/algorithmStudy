# Please write your code here.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def empty(self):
        return not self.items
    
    def pop(self):
        if self.empty():
            return False
        else:
            return self.items.pop()

    # size, top 생략

S = Stack()

str = input()

for i in range(len(str)):
    if str[i] == "(":
        S.push("(")
    else:
        if S.empty() == True:
            S.push(1)
            break
        else:
            S.pop()
            

if S.empty() == False:
    print("No")
else:
    print("Yes")