n, m = map(int,input().split())
a = [list(input()) for _ in range(n)]

def check_in_row(a, n, m):
    row_cnt = 0
    link = 0

    for i in range(n):
        for j in range(m):
            if a[i][j] == "-":
                link = 1                
                if j == m - 1:
                    row_cnt += 1
                    link = 0
            else:
                if link == 1:
                    row_cnt += 1
                    link = 0
    
    return row_cnt

def check_in_col(a, n, m):
    col_cnt = 0
    link = 0
    
    
    for j in range(m):
        for i in range(n):
            if a[i][j] == "|":
                link = 1
                if i == n - 1:
                    col_cnt += 1
                    link = 0
            else:
                if link == 1:
                    col_cnt += 1
                    link = 0

    return col_cnt

print(check_in_row(a,n,m)+check_in_col(a,n,m))