n = int(input())
nums = list(map(int,input().split()))
operators = list(map(int,input().split()))

max_sum = -10**9
min_sum =  10**9
opr_choose = []

def calculate():
    global max_sum, min_sum
    total = nums[0]
    for opr, num in zip(opr_choose, nums[1:]):
        if opr == 0:
            total += num
        elif opr == 1:
            total -= num
        elif opr == 2:
            total *= num
        else:
            total = int(total/num)
    max_sum = max(max_sum, total)
    min_sum = min(min_sum, total)
        

def choose(curr_num):
    if curr_num == n - 1:
        calculate()
        return

    for num in range(4):
        if operators[num] != 0:
            operators[num] -= 1
            opr_choose.append(num)
            choose(curr_num + 1)
            operators[num] += 1
            opr_choose.pop()

choose(0)
print(max_sum)
print(min_sum)