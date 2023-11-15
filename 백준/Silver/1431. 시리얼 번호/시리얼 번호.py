n = int(input())
guitar = [list(input()) for _ in range(n)]
guitar.sort()
for g in guitar:
    k = 0;
    for i in g:
        if i.isdigit():
            k += int(i)
    g.append(k)

guitar.sort(key = lambda x: (len(x), x[-1]))
for g in guitar:
    ans = g
    del ans[-1]
    print(''.join(ans))
