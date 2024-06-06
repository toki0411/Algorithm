import heapq
N = int(input())
pq = []
for _ in range(N):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(pq) < N:
            heapq.heappush(pq, num)

        elif pq[0] < num:
            heapq.heappop(pq)
            heapq.heappush(pq, num)

print(pq[0])