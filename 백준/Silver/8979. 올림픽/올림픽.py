n, k = map(int, input().split())
score = [list(map(int, input().split())) for _ in range(n)]
score.sort(key = lambda x:(-x[1], -x[2], -x[3]))
target = 0
for i in range(len(score)):
    if score[i][0] == k:
        target = score[i][1:]
        break
for i in range(len(score)):
    if target == score[i][1:]:
        print(i+1)
        break

