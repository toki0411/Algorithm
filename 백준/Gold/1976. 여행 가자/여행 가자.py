import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

def findParent(cur):
    if parent[cur] == cur:
        return cur
    elif parent[cur] != cur:
        parent[cur] = findParent(parent[cur])
        return parent[cur]
def union(x, y):
    x = findParent(x)
    y = findParent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(i+1, n):
        if arr[j] == 1:
            union(i+1, j+1)

travel = list(map(int, input().split()))
prev = -1
key = True
for i in range(len(travel)):
    p = findParent(travel[i])
    if prev == -1:
        prev = p
    else:
        if prev != p:
            key = False
            break;
print("YES" if key else "NO")