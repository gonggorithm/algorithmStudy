from collections import deque

def bfs(start, target):
    MAX = 100001
    dist = [-1] * MAX
    dist[start] = 0

    dq = deque()
    dq.append(start)

    while dq:
        curr = dq.popleft()

        if curr == target:
            return dist[curr]

        # 순간이동: 가중치 0 → 먼저 처리
        if 0 <= curr * 2 < MAX and dist[curr * 2] == -1:
            dist[curr * 2] = dist[curr]
            dq.appendleft(curr * 2)

        # 걷기: 가중치 1
        for next_pos in [curr - 1, curr + 1]:
            if 0 <= next_pos < MAX and dist[next_pos] == -1:
                dist[next_pos] = dist[curr] + 1
                dq.append(next_pos)

N, K = map(int, input().split())
print(bfs(N, K))