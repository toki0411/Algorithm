def solution(routes):
    routes = sorted(routes, key = lambda x: x[1])
    cnt = 1
    last_camera = routes[0][1]
    for i in range(1, len(routes)):
        start, end = routes[i][0], routes[i][1]
        if last_camera < start:
            cnt += 1
            last_camera = end
    return cnt