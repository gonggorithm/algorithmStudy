n = int(input())
arr = list(map(int, input().split()))

for i in range(1,len(arr)): #1부터 시작하는 것 주의
    j=i-1 #sorted 
    tmp=arr[i] 
    while j>=0 and arr[j]>tmp: 
        arr[j+1]=arr[j] #오른쪽으로 시프트
        j-=1 #인덱스 왼쪽으로 시프트 
    arr[j+1]=tmp 

arr_final=' '.join(str(x) for x in arr)
print(arr_final)
