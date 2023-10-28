def fibonacci():
    fibo = [0,1]
    for i in range(2, 100001):
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo
    
def solution(n):
    ans = fibonacci()
    return ans[n] % 1234567