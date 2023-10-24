from collections import deque

def solution(board):
    n = len(board)
    def bfs(x, y, cost, direction):
        graph = [[0]* n for _  in range(n)]
        dx = [-1, 1, 0, 0]; dy = [0, 0, -1, 1]
        for i in range(n):
            for j in range(n):
                graph[i][j] = board[i][j]
        q = deque([(x, y, cost, direction)])

        while q:
            x, y, cost, direction = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n :
                    #cost 계산
                    if direction == i:
                        newcost = cost + 100
                    else:
                        newcost = cost + 600
                    if (graph[nx][ny] == 0 or graph[nx][ny] > newcost):
                        q.append((nx, ny, newcost, i))
                        graph[nx][ny] = newcost
        return graph[n - 1][n - 1]
    return min(bfs(0,0,0,1),bfs(0,0,0,3))