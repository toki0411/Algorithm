from bisect import bisect_right
def solution(prices):
    ans = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            ans[i] +=1
            if prices[i] > prices[j] :
                break
    return ans