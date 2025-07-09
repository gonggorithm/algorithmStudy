import sys

n, m = map(int,input().split())
a = [list(input()) for _ in range(n)]


def row_check(a,n,m):
    count = 0
    link = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == '-':
                link = 1
                if j == m - 1:
                    count += 1
                    link = 0
            else:
                if link == 1:
                    count += 1
                    link = 0
    return count
            
def column_check(a,n,m):
    count = 0
    link = 0
    for j in range(m):
        for i in range(n):
            if a[i][j] == '|':
                link = 1
                if i == n - 1:
                    count += 1
                    link = 0
            else:
                if link == 1:
                    count += 1
                    link = 0
    return count

x = row_check(a,n,m)
y = column_check(a,n,m)

print(x+y)

sys.exit(0)