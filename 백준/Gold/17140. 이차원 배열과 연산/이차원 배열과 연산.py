R, C, K = map(int, input().split());
R -= 1;
C -= 1
key = False
graph = [list(map(int, input().split())) for _ in range(3)]
for time in range(101):
    if 0 <= R < len(graph) and 0 <= C < len(graph[0]) and graph[R][C] == K:
        key = True
        break
    rmode = 1
    if len(graph) < len(graph[0]):  # 열모드
        rmode = 0
        graph = list(map(list, zip(*graph)))

    max_cnt = 0
    for i in range(len(graph)):
        d = {}
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                continue
            if graph[i][j] not in d:
                d[graph[i][j]] = 1
            else:
                d[graph[i][j]] += 1
        # print(d)
        sorted_d = sorted(d.items(), key=lambda x: (x[1], x[0]))
        new = []
        for lst in sorted_d:
            for n in lst:
                new.append(n)
        graph[i]=new
        max_cnt = max(max_cnt, len(graph[i]))

    max_cnt = min(max_cnt, 100)
    for i in range(len(graph)):
        while len(graph[i]) < max_cnt:  # 0으로 채워야함
            graph[i].append(0)
        while len(graph[i]) > max_cnt:  # 뒤부터 지워야함
            graph[i].pop()

    if rmode == 0:  # 열모드 였다면 원상복구!!
        graph = list(map(list, zip(*graph)))
if not key:
    print(-1)
else:
    print(time)