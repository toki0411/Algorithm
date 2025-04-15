import sys
graph = [[0] * 26 for _ in range(26)]
n = int(input())
for i in range(n):
    s = input()
    graph[ord(s[0]) - ord('a')][ord(s[-1]) - ord('a')] = 1
visited = [[0] * 26 for _ in range(26)]
key = False
def dfs(idx, end):
    global key
    if idx == end:
        key = True
        return
    for i in range(26):
        if graph[idx][i] == 1 and not key:
            dfs(i, end)

m = int(input())
for i in range(m):
    s = input()
    dfs(ord(s[0]) - ord('a'), ord(s[-1]) - ord('a'))
    if key :
        print("T")
    else:
        print("F")
    key = False