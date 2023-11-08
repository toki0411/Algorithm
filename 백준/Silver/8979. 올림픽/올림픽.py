n, k = map(int, input().split())
score = [list(map(int, input().split())) for _ in range(n)]
score.sort(key = lambda x:(-x[1], -x[2], -x[3]))

prev_gold = prev_silver = prev_bronze = -1; dict = {}; cnt = 0; rank = 1
for i in range(len(score)):
    gold , silver , bronze = score[i][1], score[i][2], score[i][3]
    idx = score[i][0]
    if prev_gold ==gold and prev_silver == silver and prev_bronze == bronze:
        cnt += 1
        dict[idx] = dict[prev_idx]
    else:
        if cnt > 1: #앞에 중복이 있을 경우
            rank -=1
            dict[idx] = cnt + rank
        else:
            dict[idx] = rank
            rank += 1
        cnt = 1
    prev_idx,prev_gold, prev_silver, prev_bronze = score[i][0],score[i][1], score[i][2], score[i][3]

print(dict[k])
