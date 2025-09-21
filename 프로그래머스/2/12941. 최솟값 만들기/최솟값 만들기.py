def solution(A,B):
    answer = 0
    smallA = sorted(A)
    bigA = sorted(A, reverse=True)
    smallB = sorted(B)
    bigB = sorted(B, reverse=True)
    
    tmp1 = 0
    tmp2 = 0
    for i in range(len(A)):
        tmp1 += bigA[i] * smallB[i] 
        tmp2 += smallA[i] * bigB[i]
    answer = min(tmp1, tmp2)
    return answer