import sys
input = sys.stdin.readline
def dfs(n, s, num):
    if num == n :
        if eval(s.replace(' ', '')) == 0:
            print(s)
        return

    dfs(n, s + ' ' + str(num+1), num + 1)
    dfs(n, s + '+' + str(num + 1), num + 1)
    dfs(n, s + '-' + str(num + 1), num + 1)

T = int(input())
for tc in range(T):
    n = int(input())
    dfs(n, "1", 1)
    print()