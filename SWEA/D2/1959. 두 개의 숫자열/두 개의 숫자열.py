t = int(input())
for t_ in range(1, t + 1):
    n, m = map(int,input().split())
    ans = 0
    narr = list(map(int, input().split()))
    marr = list(map(int, input().split()))

    if len(narr) < len(marr) :
        for i in range(len(marr)-len(narr) + 1):
            tmp = 0
            for j in range(len(narr)):
                tmp += (narr[j] * marr[i+j])
            ans = max(tmp, ans)
    else :
        for i in range(len(narr)-len(marr) + 1):
            tmp = 0
            for j in range(len(marr)):
                tmp += (narr[i+j] * marr[j])
            ans = max(tmp, ans)

    print('#{} {}'.format(t_, ans))