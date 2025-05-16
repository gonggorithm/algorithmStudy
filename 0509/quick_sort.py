n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def selection_pivot(arr,low,high):
    p_index = 0
    if len(arr) <= 3:
        pivot = arr[high]
        p_index = high
    else:
        first = arr[low]
        mid = arr[(low+high)//2]
        last = arr[high]

        medium = mid
        p_index = (low+high)//2

        if medium <= first and medium <= last:
            if first <= last:
                medium = first
                p_index = low
            else:
                medium = last
                p_index = high
        elif medium >= first and medium >= last:
            if first <= last:
                medium = first
                p_index = low
            else:
                medium = last
                p_index = high
        pivot = medium
    return pivot, p_index

def partition(arr, low, high):
    pivot = selection_pivot(arr,low,high)[0]
    i = low-1
    arr[selection_pivot(arr,low,high)[1]],arr[high] = arr[high],arr[selection_pivot(arr,low,high)[1]]
    for j in range(low,high):
        if arr[j] <= pivot:
            i +=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quick_sort(arr,low,high):
    if low < high:
        pos = partition(arr,low,high)
        quick_sort(arr,low,pos-1)
        quick_sort(arr,pos+1,high)


quick_sort(arr,0,len(arr)-1)
print(*arr)