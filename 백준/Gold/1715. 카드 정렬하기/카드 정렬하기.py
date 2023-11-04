import heapq
n = int(input())
card = [int(input()) for _ in range(n)]
if n == 1:
    print(0)
else :
    ans = 0
    pq = []
    for c in card:
        heapq.heappush(pq, c)
    while len(pq) > 1:
        x = heapq.heappop(pq)
        y = heapq.heappop(pq)
        ans += (x+y)
        heapq.heappush(pq, x+y)
    print(ans)
