def solution(sequence, k):
    start = end = 0; ans = []
    prev_start =0; prev_end = len(sequence)
    val = sequence[0]
    while end < len(sequence):
        if val == k:
            if abs(start - end) < abs(prev_start - prev_end):
                prev_start = start; prev_end = end
            end += 1
            if end >= len(sequence):
                break
            else:
                val += sequence[end]
        else:
            if val < k:
                end += 1
                if end >= len(sequence):
                    break
                else:
                    val += sequence[end]
            else:
                val -= sequence[start]
                start += 1
    return [prev_start, prev_end]