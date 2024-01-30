n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
ans = ""
def solution(x, y, len) :

    # print(x, y, len)
    global ans;
    key = allCheck(x, y, len)
    if key:
        ans += str(graph[x][y]);
        return;

    elif key == False:
        range = len // 2;
        if x + range < n and y + range < n and x >= 0 and y >= 0 and range >= 1:
            ans += '('
            solution(x, y, range)
            solution(x, y + range, range)
            solution(x + range, y, range)
            solution(x + range, y + range, range)
            ans += ')'

def allCheck(x, y, len):
    #모두 같은 항인지 체크
    target = graph[x][y]
    for i in range(x, x+len):
        for j in range(y, y + len):
            if graph[i][j] != target:
                return False

    return True

solution(0,0,n)
print(ans)
