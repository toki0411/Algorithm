import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)
MAX = 1000001
n = int(input())
visited = [-1] * (MAX)

q = deque([n])  # pop메서드의 시간복잡도가 낮은 덱 내장 메서드를 이용한다
visited[n] = n  # 해당 V 값을 방문처리

while q:
    x = q.popleft()
    if x % 3 ==0 and visited[x//3]==-1 and x//3 > 0:
        q.append(x//3)
        visited[x//3] = x
    if x % 2 ==0 and visited[x//2]==-1 and x//2 > 0:
        q.append(x//2)
        visited[x//2] = x
    if visited[x-1]==-1 and x-1 > 0:
        q.append(x-1)
        visited[x-1] = x
if n == 1:
    print(0)
    print(1)
else :
    ans = []
    ans.append(1)
    tmp = visited[1]
    cnt = 1
    while 1:
        if tmp == n:
            ans.append(tmp)
            break
        ans.append(tmp)
        cnt += 1
        tmp = visited[tmp]
    ans.reverse()
    print(cnt)
    for i in ans:
        print(i, end=" ")
