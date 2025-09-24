def dfs(x, visited, graph):
    visited[x] = True
    cnt = 1  # 현재 노드 자신
    for i in range(len(graph)):
        if not visited[i] and graph[x][i] == 1:
            cnt += dfs(i, visited, graph)
    return cnt

def solution(n, wires):
    global visited, graph, cnt
    answer = 1e9
    graph = [[0] * (n) for _ in range(n)]
    visited = [0] * (n)
    for i in range(len(wires)):
        x = wires[i][0] - 1
        y = wires[i][1] - 1
        graph[x][y] = 1
        graph[y][x] = 1
        
    for i in range(len(wires)):
        x = wires[i][0] - 1
        y = wires[i][1] - 1
        graph[x][y] = 0
        graph[y][x] = 0
        visited = [0] * (n)
        a = 0; b = 0;
        for j in range(n):
            if not visited[j]:
                cnt = 1
                tmp = dfs(j, visited, graph)
                if a == 0 :
                    a = tmp
                else:
                    b = tmp
        if a != 0 and b != 0:
            answer = min(abs(a-b), answer)
        graph[x][y] = 1
        graph[y][x] = 1
    
    return answer