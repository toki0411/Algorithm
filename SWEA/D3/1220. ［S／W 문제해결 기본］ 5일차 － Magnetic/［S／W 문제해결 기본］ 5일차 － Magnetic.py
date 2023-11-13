
for tc in range(1, 11):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    ans = 0
    for i in range(n):
        flag = 0
        for j in range(n):
            if graph[j][i] == 1:
                flag = 1
            elif graph[j][i] == 2:
                if flag:
                    ans += 1
                    flag = 0
    print('#{} {}'.format(tc, ans))

    #1020101
    # 0200000
    # 0010010
    # 0000122
    # 0000010
    # 0021021
    # 0012202