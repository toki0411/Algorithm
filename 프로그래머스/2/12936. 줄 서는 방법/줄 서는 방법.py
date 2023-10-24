import math
def solution(n, k):
    num = [i for i in range(1, n + 1)]; ans = []
    while n :
        q = (k-1) // math.factorial(n-1)
        ans.append(num.pop(q))
        k = k % math.factorial(n-1)
        n -= 1
    return ans