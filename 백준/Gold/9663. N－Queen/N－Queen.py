n = int(input())
visited = [0] * n  #가로
location = [0] * n  #세로
def dfs(depth, n):
    global ans
    if depth == n:
        ans += 1
        return
    for i in range(n):
        if not visited[i]:
            location[depth] = i
            if check(depth):
                visited[i] = 1
                dfs(depth+1, n)
                visited[i] = 0
def check(x):
    for i in range(x):
        if location[i]== location[x] or abs(i-x) == abs(location[i]-location[x]):  #같은 열 혹은 대각선(행의 차와 열의 차가 같음)
            return False
    return True
ans = 0
dfs(0, n)

print(ans)