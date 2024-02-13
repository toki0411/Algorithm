import heapq

def solve():
    beer = []
    case = []
    sum = 0
    n, m, k = map(int, input().split())
    for _ in range(k):
        v, c = map(int, input().split())
        beer.append((v, c))
    beer.sort(key=lambda x: (x[1], -x[0]))
    for b in beer:
        if len(case) < n:
            heapq.heappush(case, b)
            sum += b[0]
            if len(case) == n:
                if sum >= m:
                    return b[1]
                else:
                    sum -= heapq.heappop(case)[0]
    return -1
print(solve())