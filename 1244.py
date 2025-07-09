import sys

def solve():
    n = int(sys.stdin.readline())
    s = list(map(int, sys.stdin.readline().split()))
    num_student = int(sys.stdin.readline())
    gender_actions = [list(map(int, sys.stdin.readline().split())) for _ in range(num_student)]

    def toggle(idx):
        s[idx] = 1 - s[idx]

    def male_switch(start_num):
        for i in range(start_num - 1, n, start_num):
            toggle(i)

    def female_switch(center_num):
        center_idx = center_num - 1 

        toggle(center_idx)

        for i in range(1, n):
            left_idx = center_idx - i
            right_idx = center_idx + i

            if left_idx >= 0 and right_idx < n:
                if s[left_idx] == s[right_idx]:
                    toggle(left_idx)
                    toggle(right_idx)
                else:
                    break
            else:
                break

    for action_type, num_or_idx in gender_actions:
        if action_type == 1:
            male_switch(num_or_idx)
        else:
            female_switch(num_or_idx)

    for i in range(n):
        print(s[i], end=' ')
        if (i + 1) % 20 == 0:
            print()
    if n % 20 != 0 and n > 0:
        print()

solve()