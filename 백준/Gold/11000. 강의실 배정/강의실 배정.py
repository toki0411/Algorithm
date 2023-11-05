import heapq
n = int(input())
room = [list(map(int,input().split())) for _ in range(n)]
ans = 0; pq =[]
room.sort()
heapq.heappush(pq, room[0][1])

for i in range(1, len(room)):
    if pq[0] <= room[i][0]:
        heapq.heappop(pq)
    heapq.heappush(pq, room[i][1])
print(len(pq))