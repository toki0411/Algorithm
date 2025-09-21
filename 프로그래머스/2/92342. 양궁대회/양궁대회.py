def combination_replacement(cnt, start, limit, arr, info):  # 중복조합
    if (cnt == limit):
        score(arr, info)
        return
    for i in range(start, 11):
        arr[cnt] = i
        combination_replacement(cnt + 1, i, limit, arr, info)


def score(arr, info):
    lion_score = [0] * 11
    for i in arr:
        lion_score[10 - i] += 1
    # print(arr, lion_score)
    global answer, answer_value
    lion = 0
    apeach = 0
    grade = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    for i in range(11):
        if lion_score[i] == 0 and info[i] == 0:
            continue
        if lion_score[i] > info[i]:
            lion += grade[i]
        elif lion_score[i] <= info[i]:
            apeach += grade[i]

    if lion > apeach:
        if answer_value < (lion-apeach):
            answer_value = (lion-apeach)
            answer = lion_score
        elif (lion-apeach) == answer_value:
            if check(lion_score, answer):  # 가장 낮은 점수를 많이 맞힌
                answer_value = (lion-apeach)
                answer = lion_score
    return

def check(lion, ans):
    for i in range(10, -1, -1):
        if lion[i] > ans[i]:
            return True
        elif lion[i] < ans[i]:
            return False
def solution(n, info):
    global answer, answer_value
    answer = [0] * 11
    answer_value = 0
    arr = [0] * n
    combination_replacement(0, 0, n, arr, info)
    if sum(answer) == 0:
        return [-1]
    else:
        return answer
