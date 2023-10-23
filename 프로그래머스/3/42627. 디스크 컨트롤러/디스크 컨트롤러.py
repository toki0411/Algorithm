import heapq
def solution(jobs):
    heap = []; cnt = 0
    start, time = -1, 0
    sum_time = 0
    while cnt < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for i in jobs:
            if start < i[0] <= time:
                heapq.heappush(heap, [i[1], i[0]])

        if len(heap) > 0: # 처리할 작업이 있는 경우
            tmp = heapq.heappop(heap)
            start = time
            time += tmp[0]
            sum_time += (time - tmp[1])
            cnt += 1
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            time+=1
    return sum_time // len(jobs)