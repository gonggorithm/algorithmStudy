n=int(input())

def get_ans(a):
        if a ==1:
            return 1
        
        elif a == 2:
            return 2
        
        elif a==3:
            return 4
        return get_ans(a-1) + get_ans(a-2) + get_ans(a-3)

ans=[]
for i in range(n):
    ans.append(get_ans(int(input())))

for a in ans:
     print(a)