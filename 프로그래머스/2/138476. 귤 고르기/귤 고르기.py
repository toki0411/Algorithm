def solution(k, tangerine):
    answer = 0
    dict = {}
    for t in tangerine:
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1
    arr = sorted(dict.items(), key = lambda x: -x[1])
    cnt = 0
    for i in range(len(arr)):
        if cnt + arr[i][1] >= k:
            answer += 1
            break
        
        else:
            answer += 1
            cnt += arr[i][1]
    return answer
