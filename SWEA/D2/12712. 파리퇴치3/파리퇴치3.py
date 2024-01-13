t = int(input())
for t_ in range(1, t + 1):
    ans = 0
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    plus_x = [-1, 1, 0, 0]
    plus_y = [0, 0, 1, -1]
    mul_x = [-1, 1, 1, -1]
    mul_y = [-1, -1, 1, 1]
    for i in range(n):
        for j in range(n):
            fly = graph[i][j]

            for k in range(4):
                nx = i
                ny = j
                power = m - 1
                while power > 0:
                    power -= 1
                    nx += plus_x[k]
                    ny += plus_y[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        break
                    else:
                        fly += graph[nx][ny]
            ans = max(ans, fly)

            fly = graph[i][j]
            for k in range(4):
                nx = i
                ny = j
                power = m - 1
                while power > 0:
                    power -= 1
                    nx += mul_x[k]
                    ny += mul_y[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        break
                    else:
                        fly += graph[nx][ny]
            ans = max(ans, fly)
 
    print('#{} {}'.format(t_, ans))
