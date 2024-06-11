from collections import deque
n = int(input())
balloon = list(map(int, input().split()))

q = deque()
for i, b in enumerate(balloon):
    q.append((b, i+1))
idx = 0
pop = False
while len(q) > 0:
    # print("idx : " , idx,q)
    if idx > 0:
        val = q.popleft()
        q.append(val)
        idx -= 1
    elif idx < 0:
        val = q.pop()
        q.appendleft(val)
        idx += 1
    else:
        if pop:
            val = q.pop()
            print(val[1], end=' ')
            idx = val[0]
        else:
            val = q.popleft()
            print(val[1], end = ' ')
            idx = val[0]
        if idx < 0 :
            pop = True
            idx += 1
        else:
            pop = False
            idx -= 1