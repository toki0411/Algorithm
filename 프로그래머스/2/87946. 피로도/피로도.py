def dfs(k, dungeons, cnt): #현재 피로도, 던전, 탐험 횟수
    global ans
    if cnt > ans :
        ans = cnt 
    for i in range(len(dungeons)):
        need, p = dungeons[i]
        if k >= need and not visited[i]:
            visited[i] = 1
            dfs(k - p, dungeons, cnt + 1)
            visited[i] = 0
        
def solution(k, dungeons):
    global visited, ans 
    visited = [0] * len(dungeons)
    ans = 0
    dfs(k, dungeons, 0) #현재 피로도, 던전, 탐험 횟수
    return ans