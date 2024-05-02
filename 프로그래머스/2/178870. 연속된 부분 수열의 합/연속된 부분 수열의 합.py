def solution(sequence, k):
    answer = [0, len(sequence) - 1]
    start = 0
    end = 0
    val = sequence[0]
    while end < len(sequence):
        if val == k:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            val -= sequence[start]
            start +=1
        elif val < k:
            end += 1
            if end >= len(sequence):
                break
            val += sequence[end]
        else:
            val -= sequence[start]
            start += 1  
    return answer