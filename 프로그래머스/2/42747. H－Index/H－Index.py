def solution(citations):
    n=len(citations); ans = n; 
    citations.sort(reverse= True)

    for i in range(n):
        if citations[i] < i+1:
            ans = i
            break
        
    return ans