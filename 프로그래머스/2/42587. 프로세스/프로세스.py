import heapq
from collections import deque


def solution(priorities, location):
    answer = 0
    hq = []
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))
        heapq.heappush(hq, (-priorities[i], i ))

    ans = [0] * len(priorities)
    idx = 1
    while hq:
        x = heapq.heappop(hq)
        while q:
            y = q.popleft()
            if -(x[0]) == y[0]:
                ans[y[1]] = idx;
                idx += 1
                break
            else:
                q.append(y)

    return ans[location]