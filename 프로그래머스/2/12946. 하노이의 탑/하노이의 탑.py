import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 자기 호출 개수 제한
def hanoi(n, start, goal, mid, answer):
    if n == 1:
        return answer.append([start, goal])
    hanoi(n-1, start, mid, goal, answer)
    answer.append([start, goal])
    hanoi(n-1, mid, goal, start, answer)

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer