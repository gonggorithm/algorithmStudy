n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def figure1(degree):
    shape = [[0]*2 for _ in range(2)]
    # roate_0
    shape[0][0] = 1
    shape[0][1] = 1
    shape[1][1] = 1
    print(shape)
    # rotate_90

    # rotate_180

    # rotate_270

# def figure2(n, m):

figure1(1)