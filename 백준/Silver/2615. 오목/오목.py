dx = [1, 0, 1, -1]
dy = [0, 1, 1, 1]
graph = [list(map(int, input().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        if graph[i][j] != 0:
            target = graph[i][j]
            for k in range(4):
                cnt = 1
                nx = i + dx[k]
                ny = j + dy[k]
                for l in range(4):  # 5번 한방향으로 탐색
                    if nx >= 0 and ny >= 0 and nx < 19 and ny < 19 and graph[nx][ny] == target:
                        cnt += 1
                    nx += dx[k];
                    ny += dy[k]

                if cnt == 5:  # 6번 연속인지 체크
                    if nx >= 0 and ny >= 0 and nx < 19 and ny < 19 and graph[nx][ny] == target:
                        cnt += 1
                    nx = i - dx[k]
                    ny = j - dy[k]
                    if nx >= 0 and ny >= 0 and nx < 19 and ny < 19 and graph[nx][ny] == target:
                        cnt += 1
                    if cnt == 5:
                        print(target)
                        print(i + 1, j + 1)
                        exit(0)
print(0)