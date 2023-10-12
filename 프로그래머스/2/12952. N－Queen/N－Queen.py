def check(x): #유효성 체크
    for i in range(x):
        if location[i]==location[x] or abs(i-x) == abs(location[i]-location[x]): #같은 열 혹은 대각선(행의 차와 열의 차가 같음)
            return False
    return True

def dfs(x, n): 
    global answer
    if x == n:
        answer += 1
        return 
    
    for i in range(n):
        if visited[i]: 
            continue
        location[x] = i
        if check(x):
            visited[i] = True
            dfs(x + 1, n)  
            visited[i] = False
            
def solution(n):
    global answer
    global location, visited
    location = [0] * n
    visited = [False] * n
    answer = 0
    dfs(0, n)
    return answer