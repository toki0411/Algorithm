def solution(targets):
    targets.sort(key = lambda x: x[1]); 
    before = targets[0][1]; cnt = 1
    for i in range(1, len(targets)):
        if before <= targets[i][0]:
            cnt += 1
            before = targets[i][1]
    
    return cnt