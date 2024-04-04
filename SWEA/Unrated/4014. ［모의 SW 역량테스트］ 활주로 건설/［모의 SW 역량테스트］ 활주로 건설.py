from collections import deque

T = int(input())


def checkLeft(i, j):
    target = graph[i][j]
    cnt = 0
    for k in range(j, j-X, -1): #건설 가능한지 체크
        if k < 0:
            break
        if not visited[k] and graph[i][k] == target:
            cnt += 1
        elif visited[k] and graph[i][k] == target:
            return False
        else:
            break
    if cnt >= X: #건설 시작
        for k in range(j , j-cnt, -1):
            visited[k] = 1


def checkRight(i, j):
    target = graph[i][j]
    cnt = 0
    for k in range(j, j + X):  # 건설 가능한지 체크
        if k >= N:
            break
        if not visited[k] and graph[i][k] == target:
            cnt += 1
        elif visited[k] and graph[i][k] == target:
            return False
        else:
            break
    if cnt >= X:  # 건설 시작
        for k in range(j, j + cnt):
            visited[k] = 1

for tc in range(1, T+1):
    N, X= map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    #가로 탐색
    for i in range(N):
        visited = [0] * N
        key = True
        for j in range(1, N):
            a = 1; b =1
            if abs(graph[i][j - 1] - graph[i][j]) >= 2:
                key = False
                break
            # 지대가 높아질 경우
            if graph[i][j-1] < graph[i][j] :
                a = checkLeft(i, j-1)
            # 지대가 낮아질 경우
            if graph[i][j - 1] > graph[i][j]:
                b = checkRight(i, j)
            if a == False or b == False:
                key = False
                break
        if key:
            for j in range(1, N):
                if graph[i][j - 1] < graph[i][j]:
                    if not visited[j-1]:
                        key = False
                        break
                elif graph[i][j-1] > graph[i][j]:
                    if not visited[j]:
                        key = False
                        break
        if key:
            ans += 1

    # 세로 탐색
    reversed_graph = graph[::-1]
    graph = list(zip(*reversed_graph))
    for i in range(N):
        visited = [0] * N
        key = True
        for j in range(1,N):
            a = 1;
            b = 1
            if abs(graph[i][j-1] - graph[i][j]) >= 2:
                key = False
                break
            # 지대가 높아질 경우
            if graph[i][j-1] < graph[i][j]:
                a = checkLeft(i, j-1)
            # 지대가 낮아질 경우
            if graph[i][j - 1] > graph[i][j]:
                b = checkRight(i, j)
            if a == False or b == False:
                key = False
                break
        if key:
            for j in range(1, N):
                if graph[i][j - 1] < graph[i][j]:
                    if not visited[j-1]:
                        key = False
                        break
                elif graph[i][j-1] > graph[i][j]:
                    if not visited[j]:
                        key = False
                        break
        if key:
            ans += 1

    print("#{} {}".format(tc, ans))