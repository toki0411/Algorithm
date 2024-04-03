def check():
    for i in range(6):
        for j in range(3):
            if score[i][j] != 0:
                return False
    return True


def dfs(nowTeam, nextTeam, depth):
    # print(nowTeam, nextTeam)
    global key
    if key: return
    if nextTeam == 6:
        nowTeam += 1
        nextTeam = nowTeam + 1


    if nowTeam == 5:
        if check():
            key = True
        return

    if score[nowTeam][0] > 0 and score[nextTeam][2] > 0:
        score[nowTeam][0] -= 1
        score[nextTeam][2] -= 1
        dfs(nowTeam, nextTeam + 1, depth + 1)
        score[nowTeam][0] += 1
        score[nextTeam][2] += 1

    if score[nowTeam][1] > 0 and score[nextTeam][1] > 0:
        score[nowTeam][1] -= 1
        score[nextTeam][1] -= 1
        dfs(nowTeam, nextTeam + 1, depth + 1)
        score[nowTeam][1] += 1
        score[nextTeam][1] += 1

    if score[nowTeam][2] > 0 and score[nextTeam][0] > 0:
        score[nowTeam][2] -= 1
        score[nextTeam][0] -= 1
        dfs(nowTeam, nextTeam + 1, depth + 1)
        score[nowTeam][2] += 1
        score[nextTeam][0] += 1




arr = [list(map(int, input().split())) for _ in range(4)]

for a in arr:
    score = []
    for l in range(0, 18, 3):
        score.append(a[l:l + 3])
    key = False
    dfs(0, 1, 0)
    if key:
        print(1, end=" ")
    else:
        print(0, end=" ")