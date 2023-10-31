from collections import deque
def solution(info, edges):
    visited = [0] * len(info)
    visited[0] = 1
    max_sheep = 0

    def dfs(sheep, wolf):
        nonlocal max_sheep
        if sheep > wolf:
            max_sheep = max(sheep, max_sheep)
        else:  # 양이 늑대보다 같거나 적으면
            return
        for e in edges:
            parent, child = e
            if visited[parent] and not visited[child]:
                visited[child] = 1
                if info[child]:  # 늑대
                    dfs(sheep, wolf + 1)
                else:
                    dfs(sheep + 1, wolf)
                visited[child] = 0

    dfs(1, 0)
    return max_sheep