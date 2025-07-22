def backtracking(start, arr, S):
    if len(arr) == 6:
        print(*arr)
        return

    for i in range(start, len(S)):
        arr.append(S[i])
        backtracking(i + 1, arr, S)
        arr.pop()

while True:
    array = list(map(int, input().split()))
    k = array[0]

    if k == 0:
        break

    S = array[1:]
    backtracking(0, [], S)
    print()
    