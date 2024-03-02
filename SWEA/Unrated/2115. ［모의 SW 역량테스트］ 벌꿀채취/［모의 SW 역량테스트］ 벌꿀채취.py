
T = int(input())


def subset(cnt, tmp):
    global maxVal
    if cnt == m:
        a = 0
        for i in range(m):
            if ans[i] == 1:
                a+= tmp[i]
        if a > c: return
        val = 0
        for i in range(m):
            if ans[i] == 1:
                val += (tmp[i]*tmp[i])

        maxVal = max(val, maxVal)
        return
    ans[cnt] = 1
    subset(cnt+1, tmp)
    ans[cnt] = 0
    subset(cnt+1, tmp)

for tc in range(1, T + 1):
    n,m,c = map(int, input().split())
    honey = []
    graph = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n-m+1):
            tmp = graph[i][j:j+m]
            ans = [0] * m
            if sum(tmp) > c:
                maxVal = 0
                subset(0, tmp)
                honey.append((maxVal, i, j))
            else:
                val = 0
                for l in range(len(tmp)):
                    val += (tmp[l]*tmp[l])
                honey.append((val, i, j))
    honey.sort(key = lambda x : -x[0])
    # print(honey)
    total_honey = honey[0][0]
    x = honey[0][1]
    # print(honey)
    for i in range(1,len(honey)):
        if x != honey[i][1]:
            total_honey += honey[i][0]
            break

    print('#{} {}'.format(tc, total_honey))
