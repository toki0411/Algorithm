t = int(input())
for tc in range(1, t+1):
    target = list(input())
    val = ['0'] * len(target)
    ans = 0
    for i in range(len(target)):
        if val[i] != target[i]:
            ans += 1
            for j in range(i, len(target)):
                val[j] = target[i]


    print('#{} {}'.format(tc, ans))

