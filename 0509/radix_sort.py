n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
max_k = 6
base = 10

def radix_sort():
    global arr

    pos = 1
    for _ in range(max_k):
        new_arr = [[] for _ in range(base)]
        # 파이썬은 arr[][] 은 error

        for i in range(n):
            digit = (arr[i] // pos) % base
            new_arr[digit].append(arr[i])
        
        arr = []

        for digit in range(base):
            for elem in new_arr[digit]:
                arr.append(elem)
        
        pos *= base

radix_sort()

for elem in arr:
    print(elem, end=" ")