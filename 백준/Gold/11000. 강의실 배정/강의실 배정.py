import heapq
pq = []
q = []
n = int(input())

for _ in range(n):
    s, t = map(int, input().split())
    q.append([s,t])
q.sort()

heapq.heappush(pq, q[0][1])
for i in range(1, n):
    if q[i][0] < pq[0]:
        heapq.heappush(pq, q[i][1])
    else:
        heapq.heappop(pq)
        heapq.heappush(pq, q[i][1])
print(len(pq))






