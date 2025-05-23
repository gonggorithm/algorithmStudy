n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def selection_sort(arr):
    size = len(arr)

    for i in range(size-1):
        min = i
        for j in range(i+1,size):
            if arr[j] < arr[min]:
                min = j
        tmp = arr[i]
        arr[i] = arr[min]
        arr[min] = tmp

    return arr

for num in selection_sort(arr):
    print(num, end = " ")