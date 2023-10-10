def solution(answers):
    a = [1, 2, 3, 4, 5];     answer = []
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a_idx, b_idx, c_idx = 0, 0, 0
    a_cnt, b_cnt, c_cnt = 0, 0, 0
    for i in answers:
        if i == a[a_idx]:
            a_cnt += 1
        if i == b[b_idx]:
            b_cnt += 1
        if i == c[c_idx]:
            c_cnt += 1
        a_idx +=1; b_idx +=1; c_idx +=1
        if a_idx >= len(a):
            a_idx = 0
        if b_idx >= len(b):
            b_idx = 0
        if c_idx >= len(c):
            c_idx = 0

    val = max(a_cnt, b_cnt, c_cnt)
    if val == a_cnt:
        answer.append(1)
    if val == b_cnt:
        answer.append(2)
    if val == c_cnt:
        answer.append(3)

    return answer