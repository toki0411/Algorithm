from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    graph = [['.' for _ in range(m+2)]]
    document = 0
    keys = []
    for i in range(n):
        tmp = list(input())
        if i == 0 or i == n-1:
            for j in range(m):
                if tmp[j] == '$':
                    document += 1
                    tmp[j] = '.'
                elif 97 <= ord(tmp[j]) <= 122:  #소문자
                    keys.append(tmp[j])
                    tmp[j] = '.'
        if tmp[0] == '$':
            document += 1
            tmp[0] = '.'
        elif 97 <= ord(tmp[0]) <= 122:  # 소문자
            keys.append(tmp[0])
            tmp[0] = '.'
        if tmp[-1] == '$':
            document += 1
            tmp[-1] = '.'
        elif 97 <= ord(tmp[-1]) <= 122:  # 소문자
            keys.append(tmp[-1])
            tmp[-1] = '.'
        graph.append(['.'] + tmp + ['.'])

    graph.append(['.' for _ in range(m+2)])

    tmp = list(input())
    if tmp[0] != '0':
        for k in tmp:
            keys.append(k)

    visited = [[0] * (m+2) for _ in range(n+2)]
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        # print(x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n+2 or ny >= m+2:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == '.':
                q.append((nx, ny))
                visited[nx][ny] = 1
            elif 97 <= ord(graph[nx][ny]) <= 122:  #소문자 (열쇠)
                if graph[nx][ny] not in keys:
                    visited = [[0] * (m + 2) for _ in range(n + 2)]  # 방문 초기화
                    keys.append(graph[nx][ny])
                    graph[nx][ny] = '.'
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                else:
                    graph[nx][ny] = '.'
                    q.append((nx, ny))
                    visited[nx][ny] = 1
            elif 65 <= ord(graph[nx][ny]) <= 90:  #대문자 (문)
                key = chr(ord(graph[nx][ny]) + 32)
                if key in keys:
                    graph[nx][ny] = '.'
                    q.append((nx, ny))
                    visited[nx][ny] = 1
            elif graph[nx][ny] == '$':
                document += 1
                graph[nx][ny] = '.'
                q.append((nx, ny))
    print(document)