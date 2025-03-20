import sys
input = sys.stdin.readline
global n;
def dfs(s, num):
    if num == n :
        if eval(s.replace(' ', '')) == 0:
            print(s)
        return

    dfs(s + ' ' + str(num+1), num + 1)
    dfs(s + '+' + str(num + 1), num + 1)
    dfs(s + '-' + str(num + 1), num + 1)

T = int(input())
for tc in range(T):
    n = int(input())
    dfs( "1", 1)
    print()