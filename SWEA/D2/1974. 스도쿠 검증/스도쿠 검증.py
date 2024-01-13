t = int(input())
index_arr = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
for t_ in range(1, t + 1):
    ans = 1
    graph = [list(map(int, input().split())) for _ in range(9)]
    #가로 체크
    for i in range(9):
        visited = [0] * 10
        for j in range(9):
            if visited[graph[i][j]] == 1:
                ans = 0
                break
            else:
                visited[graph[i][j]] = 1
        # 세로 체크
        visited = [0] * 10
        for j in range(9):
            if visited[graph[j][i]] == 1:
                ans = 0
                break
            else:
                visited[graph[j][i]] = 1

        visited = [0] * 10
        x, y = index_arr[i]
        for j in range(x, x+3):
            for k in range(y, y+3):
                if visited[graph[j][k]] == 1:
                    ans = 0
                    break
                else:
                    visited[graph[j][k]] = 1
        if ans == 0:
            break


    print('#{} {}'.format(t_, ans))
