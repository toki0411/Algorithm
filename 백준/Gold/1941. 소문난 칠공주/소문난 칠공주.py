from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(depth, start):
    global ans
    if depth == 7:
        if bfs() :
            ans += 1
        return
    for i in range(start, 25):
        visited[i // 5][i % 5] = 1
        dfs(depth + 1, i + 1)
        visited[i // 5][i % 5] = 0

def bfs(): #이어져 있고, 솜파의 승리인지 체크
    som = 0; doyeon =0
    visited2 = [[0] * 5 for _ in range(5)]
    x = 0; y = 0
    for i in range(5):
        for j in range(5):
            if visited[i][j]:
                visited2[i][j] = visited[i][j]
                x = i;  y = j
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5: continue
            if visited2[nx][ny]:
                visited2[nx][ny] = 0
                q.append((nx, ny))
                if graph[nx][ny] == 'S': som +=1
                else: doyeon += 1
    if som + doyeon != 7: return False
    elif som < 4: return False
    else: return True

graph = [list(input()) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
ans = 0

dfs(0, 0)
print(ans)