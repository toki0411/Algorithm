import sys
sys.stdin.readline
from collections import deque
n, T = map(int, input().split())
rock = set()

for _ in range(n):
    a,b = map(int, input().split())
    rock.add((a,b))

key = False
q = deque()
q.append((0,0, 0))
idx = set()
while q:
    x, y, cnt = q.popleft()
    if y == T :
        print(cnt)
        key = True
        break
    for i in range(-2, 3):
        for j in range(-2, 3):
            nx = x + i
            ny = y + j
            if (nx, ny) in rock:
                q.append((nx, ny, cnt + 1))
                rock.remove((nx, ny))

if not key:
    print(-1)