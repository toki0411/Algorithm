import sys
sys.setrecursionlimit(10**6)
def solution(tickets):
    answer = []
    visited = [False] * len(tickets)

    def dfs(V, path):
        #백트래킹 종료
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return

        for idx, ticket in enumerate(tickets):
            if V == ticket[0] and not visited[idx]:
                visited[idx] = True;
                # path.append(ticket[1])
                dfs(ticket[1], path+[ticket[1]])
                visited[idx] = False

    dfs('ICN', ["ICN"])
    answer.sort()
    return answer[0]