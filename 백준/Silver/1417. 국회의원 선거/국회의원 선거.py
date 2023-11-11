import heapq
n = int(input())
vote = [int(input()) for _ in range(n)]
hq = []; dasom = vote[0]; ans = 0
for i in range(1,n):
    heapq.heappush(hq, (-vote[i], vote[i]))

while hq:
    x = heapq.heappop(hq)
    val = x[1]
    if val >= dasom:
        dasom+=1
        ans +=1
        val -=1
        heapq.heappush(hq, (-val, val))
print(ans)