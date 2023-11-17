t = int(input())
for tc in range(1, t+1):
    graph = [list(map(int, input().split())) for _ in range(9)]
    reversed_graph = graph[::-1]
    rotated = list(zip(*reversed_graph))
    check = [0] * 10
    ans = 0; key = False
    index_arr = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
    for i in range(9):
        check = [0] * 10
        arr = graph[i]
        for j in range(9):
            if check[arr[j]] == 1:
                key = True
                break
            else:
                check[arr[j]] = 1

        check = [0] * 10
        arr2 = rotated[i]
        for j in range(9):
            if check[arr2[j]] == 1:
                key = True
                break
            else:
                check[arr2[j]] = 1

        check = [0] * 10
        x, y = index_arr[i]
        for j in range(x, x+3):
            for k in range(y, y+3):
                if check[graph[j][k]] == 1:
                    key = True
                    break
                else:
                    check[graph[j][k]] = 1
            if key:
                break
        if key:
            break
    if key:
        ans = 0
    else:
        ans = 1
    print('#{} {}'.format(tc,ans))

