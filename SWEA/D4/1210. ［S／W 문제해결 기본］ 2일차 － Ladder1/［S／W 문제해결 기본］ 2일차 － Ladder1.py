from collections import deque

dx = [0, 0, -1]
dy = [1, -1, 0]
for tc in range(1,11):
    t = int(input());    n = 100
    ans = target_x = target_y = 0
    q=deque()
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * 100 for _ in range(100)]
    # 2 찾기
    for i in range(100):
        if graph[n-1][i] == 2:
            target_x = n-1
            target_y = i
            visited[target_x][target_y]=1
            q.append([target_x, target_y])
            break

    while q:
        x, y = q.popleft()
        if x == 0:
            ans = y
            break
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append([nx, ny])
                break
    print('#{} {}'.format(t, ans))