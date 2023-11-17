from collections import deque


def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        x = q.popleft()
        seq = 0
        for i in q:
            seq += 1
            if x > i:
                break
        answer.append(seq)
    return answer
print(solution([1,2,3,2,3]))