n, m = map(int, input().split())
if n == 0:
    print(0)
    exit(0)
    
box = list(map(int, input().split()))

weight = 0
box_cnt = 1
for b in box:
    if weight + b > m:
        box_cnt += 1
        weight = b
    else:
        weight += b
print(box_cnt)