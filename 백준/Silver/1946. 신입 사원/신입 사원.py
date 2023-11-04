t = int(input())
for tc in range(t):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]
    score.sort()
    cnt = 1
    max_ = score[0][1]
    for i in range(1, n):
        if max_ > score[i][1]:
            
            cnt += 1
            max_ = score[i][1]

    print(cnt)


