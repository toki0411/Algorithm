import heapq
N = int(input())
meeting = []
for _ in range(N):
    start, end = map(int, input().split())
    meeting.append([start, end])
meeting.sort()

pq = []
heapq.heappush(pq, meeting[0][1])
for i in range(1,N):
    if pq[0] > meeting[i][0]: #이전 회의 끝나는 시간보다 시작시간이 먼저면
        heapq.heappush(pq, meeting[i][1])
    else:
        heapq.heappop(pq)
        heapq.heappush(pq, meeting[i][1])

print(len(pq))