n = int(input())
nums = list(map(int,input().split()))
operators = list(map(int,input().split()))

operator_choose = []
operator_map = {
    0 : "+",
    1 : "-",
    2 : "*",
    3 : "/"
}

def choose(curr_num):
    for operator in operators:
        