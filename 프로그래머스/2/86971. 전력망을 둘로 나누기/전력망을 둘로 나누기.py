from collections import deque
def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for i in range(len(wires)):
        a, b = wires[i]
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(v):
        visited =[0] * (n+1)
        visited[v] = True
        q = deque([v])
        cnt = 1
        while q:
            x = q.popleft()
            for i in range(1, n+1):
                if not visited[i] and i in graph[x]:
                    visited[i] = True
                    cnt += 1
                    q.append(i)
        return cnt
    val = 10000000
    for i in range(len(wires)):
        a, b = wires[i]
        graph[a].remove(b)
        graph[b].remove(a)
        
        val = min(abs(bfs(a) - bfs(b)), val)
        
        graph[a].append(b)
        graph[b].append(a)
        
    return val
        
    