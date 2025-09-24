from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        x = q.popleft()
        seq = 0
        for node in q:
            seq += 1
            if x > node : 
                break

        answer.append(seq)
    return answer
