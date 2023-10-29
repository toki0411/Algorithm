from collections import *
def solution(x, y, n):
    q = deque([(x,n,0)])
    visited = set()
    if x == y:
        return 0
    while q:
        x, n, cnt = q.popleft()
        visited.add(x)
        if x == y:
            return cnt
        if (x+n) <= y and x+n not in visited:
            q.append((x+n, n, cnt + 1))
            visited.add(x+n)
        if x*2 <= y and x*2 not in visited:
            q.append((x*2, n, cnt+1))
            visited.add(x*2)
        if x*3 <= y and x*3 not in visited:
            q.append((x*3, n, cnt + 1))
            visited.add(x*3)
            
    return -1