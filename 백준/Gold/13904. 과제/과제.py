n = int(input())
arr = []
tmp = 0
for _ in range(n):
    d, w = map(int, input().split())
    arr.append((d,w))
    tmp = max(tmp, d)
ans = [0] * (tmp+1)
arr.sort(key = lambda x : (-x[1], x[0]))

day = 0
for i in range(n):

    day = arr[i][0];
    score = arr[i][1]
    for d in range(day, 0, -1):
        if ans[d] == 0:
            ans[d] = score;
            break;
        elif ans[d] < score:
            ans[d] = score;
            break;


print(sum(ans))