a, b = map(int, input().split())
cnt = 0
while b > a:
    b_str = str(b)
    if b_str[-1] == '1':
        b_str = b_str[:len(b_str) -1]
        b = int(b_str)
    elif b % 2 == 0:
        b = (b // 2)
    else:
        b = 0
        break
    cnt += 1
if b < a:
    print(-1)
else:
    print(cnt+1)