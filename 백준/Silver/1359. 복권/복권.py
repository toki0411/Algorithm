import math
N, M, K = map(int, input().split())

def combination(n, m):
    if n < m: return 0
    return math.factorial(n) / (math.factorial(n-m) * math.factorial(m))

def possibility(n, m, k):
    return combination(m, k) * combination(n-m, m-k) / combination(n, m) 

answer = 0
for k in range(K, M+1):
    answer += possibility(N, M, k)

print(answer)