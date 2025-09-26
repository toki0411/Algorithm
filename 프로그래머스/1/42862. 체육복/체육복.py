def solution(n, lost, reserve):
    answer = 0
    cnt = [1] * (n+1)
    for l in lost:
        cnt[l]-=1 
    for r in reserve:
        cnt[r]+=1
    for i in range(1, n+1):
        if cnt[i] == 0:
            if i-1 > 0 and cnt[i-1] > 0:
                answer += 1
                cnt[i-1] -=1
            elif i+1 < n+1 and cnt[i+1] > 1:
                answer += 1
                cnt[i+1]-=1
        else:
            answer += 1
            cnt[i]-=1
    return answer