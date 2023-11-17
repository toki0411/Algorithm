def solution(targets):
    answer = 1
    targets.sort(key = lambda x:x[1])
    start = end = 0
    end = targets[0][1]
    for i in range(1, len(targets)):
        if targets[i][0] >= end :
            answer += 1
            end = targets[i][1]
    return answer

