def dfs(cnt):
    global ans;
    if cnt == 0:
        num_case = int(''.join(num))
        if  num_case > ans:
            ans = num_case
        return

    for i in range(0, len(num)):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]
            tmp = ''.join(num)
            if visited.get((tmp, cnt), 1):
                visited[(tmp, cnt)] = 0
                dfs(cnt - 1)
            num[i], num[j] = num[j], num[i]  #원상복구

t = int(input())
for t_ in range(1,t+1):
    ans = -1
    num, exchange = map(int, input().split())
    num = list(str(num))
    visited = {}
    dfs(exchange);
    print('#{} {}'.format(t_, ans))