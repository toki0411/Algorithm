def subset(start, depth):  #약품을 투입하는 모든 경우를 찾음. 현재 인덱스, 약품 투입 횟수
    global ans
    if depth > ans:
        return
    if check():
        ans = min(ans, depth)
        return
    if start >= N:
        return

    for i in range(start, N):
        graph2 = [0] * M
        for j in range(M):
            graph2[j] = graph[i][j]
        #약품 처리
        for j in range(M):  #A로
            graph[i][j] = 1
        subset(i + 1, depth + 1)

        for j in range(M):  #B로
            graph[i][j] = 0
        subset(i + 1, depth + 1)

        for j in range(M):
            graph[i][j] = graph2[j]

def check():
    for i in range(M):
        cnt = 1;
        for j in range(N-1):
            if graph[j][i] == graph[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= K:
                break
        if cnt < K:
            return False
    return True


T =int(input())
for tc in range(1, T+1):
    ans = 1e9
    N, M, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    subset(0,0)
    print('#{} {}'.format(tc, ans))