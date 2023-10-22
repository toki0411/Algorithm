def solution(progresses, speeds):
    store = [];
    ans = []
    for i in range(len(progresses)):
        init_percent, speed = progresses[i], speeds[i]
        day = 0
        for p in range(init_percent, 100, speed):
            day += 1
        store.append([day, i])

    max_day = sorted(store, key = lambda x:-x[0])[0][0]
    stack = []
    for i in range(1, max_day + 1):
        deploy = store[0][0]
        for j in store:
            day, dayidx = j[0], j[1]
            if day <= i:
                stack.append([day, dayidx])
            elif day > i :
                break
        if i == deploy:
            cnt = 0
            while stack:
                cnt += 1
                deployed = stack.pop()
                store.remove(deployed)
            ans.append(cnt)
    return ans