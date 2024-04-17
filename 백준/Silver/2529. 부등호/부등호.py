import sys
sys.stdin.readline
minVal = 1e10
maxVal = -1
minAns = 0
maxAns = 0
def dfs(depth, exp, arr):
    global minVal, maxVal, minAns, maxAns
    if depth == N:
        if eval(exp):
            sval = ''.join(arr)
            val = int(sval)
            if val < minVal:
                minVal = val
                minAns = sval
            elif val > maxVal:
                maxVal = val
                maxAns = sval
        return
    if op[depth] == '<':
        start = int(exp[-1])+1
        for i in range(start, 10):
            if not visited[i]:
                visited[i] = 1
                dfs(depth + 1, exp +op[depth]+ str(i), arr + str(i))
                visited[i] = 0
    elif op[depth] == '>':
        start = int(exp[-1])
        for i in range(0, start):
            if not visited[i]:
                visited[i] = 1
                dfs(depth + 1, exp + op[depth] +str(i), arr +str(i) )
                visited[i] = 0

N = int(input())
op = list(input().split())
exp = ''
visited = [0] * 10
arr = ''
for i in range(10):
    visited = [0] * 10
    visited[i] = 1
    dfs(0, exp + str(i), arr + str(i))

print(maxAns, minAns)