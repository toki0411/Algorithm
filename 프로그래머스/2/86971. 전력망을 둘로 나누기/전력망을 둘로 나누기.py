def dfs(now):
    global d, visited, graph
    d += 1
    visited[now] = 1
    for g in graph[now]:
        if not visited[g]:
            dfs(g)

def solution(n, wires):
    global d, visited, graph
    wires.sort()
    
    answer = 1e9
    for i in range(n-1):
        graph = [[] for _ in range(n+1)]
        for j in range(n-1):
            if i != j:
                a, b = wires[j][0], wires[j][1]
                graph[a].append(b)
                graph[b].append(a)
        visited = [0] * (n+1)
        diff = []
        for j in range(1, n+1):
            if not visited[j]:
                d = 0
                dfs(j)
                diff.append(d)
        # print(diff)
        if len(diff) == 2:
            answer = min(abs(diff[0] - diff[1]), answer)
    return answer