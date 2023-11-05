num = 1
while True:
    ans = 0
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    while True:
        if v >= p:
            ans += l
            v -= p
        elif l < v < p:
            ans += l
            v = 0
            break
        elif v <= l:
            ans += v
            v = 0
            break
    print("Case {}: {}".format(num, ans))
    num += 1