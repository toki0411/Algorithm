def checkLikeAdjBlank(idx):  # 1단계. 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정함. 여러개인 경우 여러개 리턴
    seat = []
    max_cnt = -1
    for i in range(n):
        for j in range(n):
            if graph[i][j] == -1:  # 빈칸이면
                cnt = 0  # 인접한 칸에 좋아하는 학생이 몇 명인지 체크
                for l in range(4):
                    nx = i + dx[l]
                    ny = j + dy[l]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
                    if graph[nx][ny] in like[arr[idx]]:
                        cnt += 1
                if cnt >= max_cnt:
                    max_cnt = cnt
                    seat.append([cnt, i, j])
    ans = []
    for i in range(len(seat)):
        if max_cnt == seat[i][0]:
            ans.append([seat[i][1], seat[i][2], seat[i][0]])
    return ans


def checkAdjBlank(adjIdx):  # 인접한 칸 중에서 비어있는 칸이 가장 많은 칸을 리턴. 여러개일 경우 여러개 리턴
    max_cnt = -1
    ans = []
    seat2 = []
    for i in range(len(adjIdx)):
        x, y = adjIdx[i][0], adjIdx[i][1]
        cnt = 0
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if graph[nx][ny] == -1:
                cnt += 1
        if cnt >= max_cnt:
            max_cnt = cnt
            seat2.append([cnt, x, y])
    for i in range(len(seat2)):
        if max_cnt == seat2[i][0]:
            ans.append([seat2[i][1], seat2[i][2], seat2[i][0]])

    return ans


def satisfied():
    h = 0
    for i in range(n):
        for j in range(n):
            cnt = 0
            for l in range(4):
                nx = i + dx[l]
                ny = j + dy[l]
                if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
                if graph[nx][ny] in like[graph[i][j]]:
                    cnt += 1
            if cnt == 1:
                h += 1
            elif cnt == 2:
                h += 10
            elif cnt == 3:
                h += 100
            elif cnt == 4:
                h += 1000
    print(h)


n = int(input())
# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = [[-1] * n for _ in range(n)]  # -1로 초기화
like = [[0, 0, 0, 0] for _ in range(n * n)]

arr = [0] * (n * n)
for i in range(n * n):
    a, b, c, d, e = map(int, input().split())
    like[a - 1] = [b - 1, c - 1, d - 1, e - 1]
    arr[i] = a - 1

for i in range(n * n):
    seat = checkLikeAdjBlank(i)
    if len(seat) > 1:
        seat = checkAdjBlank(seat)
        if len(seat) > 1:
            # seat 정렬 후 행의 번호가 가장 작고, 열의 번호가 가장 작은 칸 선택
            seat.sort(key=lambda x: (x[0], x[1]))

    graph[seat[0][0]][seat[0][1]] = arr[i]
satisfied()