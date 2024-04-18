import sys
sys.stdin.readline
def calculate():
    global max_ans
    # ㅡ 모양 1번째 블록
    for i in range(N):
        for j in range(N-3):
            tmp = 0
            for k in range(j, j+4):
                tmp += graph[i][k]
            if tmp > max_ans:
                max_ans = tmp

    # 2번째
    for i in range(N-1):
        for j in range(N-2):
            tmp = 0
            for k in range(j, j+2):
                tmp += graph[i][k]
            for k in range(j+1, j+3):
                tmp += graph[i+1][k]
            if tmp > max_ans:
                max_ans = tmp

    # ㄱ모양 3번째 블록
    for i in range(N-1):
        for j in range(N-2):
            tmp = 0
            for k in range(j, j+3):
                tmp += graph[i][k]
            tmp += graph[i+1][j+2]
            if tmp > max_ans:
                max_ans = tmp

    # 4번째 블록
    for i in range(N-1):
        for j in range(N-2):
            tmp = 0
            for k in range(j, j+3):
                tmp += graph[i][k]
            tmp += graph[i+1][j+1]
            if tmp > max_ans:
                max_ans = tmp

    # ㅁ모양 5번째 블록
    for i in range(N-1):
        for j in range(N-1):
            tmp = 0
            for k in range(j, j+2):
                tmp += graph[i][k]
                tmp += graph[i+1][k]
            if tmp > max_ans:
                max_ans = tmp


tc = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    max_ans = -9_999_999

    calculate()

    reversed_graph = graph[::-1]
    graph = list(map(list, zip(*reversed_graph)))  #90도
    calculate()

    reversed_graph = graph[::-1]
    graph = list(map(list, zip(*reversed_graph)))  #180도
    calculate()

    reversed_graph = graph[::-1]
    graph = list(map(list, zip(*reversed_graph)))  #270도
    calculate()

    print("{}. {}".format(tc, max_ans))
    tc += 1