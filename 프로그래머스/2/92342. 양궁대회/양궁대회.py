from itertools import combinations_with_replacement as cwr
def solution(n, info):
    max_gap = -1
    answer = [-1]
    arr = [0,1,2,3,4,5,6,7,8,9,10]
    for shot in cwr(arr, n):
        case = [0] * 11
        for i in shot:
            case[10-i] += 1
        apeach = lion = 0
        #점수 차이 계산
        for i in range(11):
            if info[i] == case[i] == 0:
                continue
            elif info[i] >= case[i] :
                apeach += (10 - i)
            else:
                lion += (10 - i)
        if lion > apeach and (lion - apeach) > max_gap:
            max_gap = lion - apeach
            answer = case
    return answer