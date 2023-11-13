from collections import deque
for tc in range(1, 11):
    t = int(input())
    arr = list(map(int, input().split()))
    q = deque()
    for a in arr:
        q.append(a)
    key = False
    while True:
        for i in range(1,6):
            x = q.popleft()
            if x-i <= 0:
                q.append(0)
                key = True
                break
            else:
                q.append(x-i)
        if key:
            break

    print('#{} '.format(t), end = '')
    print(*list(q))

