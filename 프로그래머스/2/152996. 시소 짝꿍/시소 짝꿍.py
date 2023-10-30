from collections import Counter


def solution(weights):
    cnt = 0
    # 중복인 경우 무조건 해당되므로 처리
    count = Counter(weights)
    for c in count:
        if count[c] >= 2:
            cnt += (count[c] * (count[c] - 1)) // 2

    # 중복을 제거
    weights = list(set(weights))
    for w in weights:
        if w * 2 / 3 in weights:
            cnt += count[w*2/3] * count[w]
        if w * 2 / 4 in weights:
            cnt += count[w*2/4] * count[w]
        if w * 3 / 4 in weights:
            cnt += count[w*3/4] * count[w]
    return cnt