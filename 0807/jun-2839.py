def get_ik(n):
    global ans
    for i in range(0,1001):
        for k in range(0,1001):
            if 3*i + 5*k == n:
                if i + k > ans:
                    ans = i + k
                    return ans
    return -1

ans= -1
n=int(input())
print(get_ik(n))