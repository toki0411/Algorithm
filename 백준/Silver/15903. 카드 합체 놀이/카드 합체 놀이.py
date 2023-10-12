import heapq
pq = []
n, m = map(int, input().split())

arr = list(map(int, input().split()))
for i in arr:
    heapq.heappush(pq, i)

for _ in range(m):
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    heapq.heappush(pq, a+b)
    heapq.heappush(pq, a+b)
print(sum(pq))