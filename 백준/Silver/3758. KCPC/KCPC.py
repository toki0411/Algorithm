T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    grade = [[0] * (k+1) for __ in range(n+1)]
    cnt = [0] * (n+1)
    time = [0] * (n+1)
    for now in range(m):
        i, j, s = map(int, input().split())
        grade[i][j] = max(s, grade[i][j])
        cnt[i] +=1
        time[i] = now

    grade_sums = [sum(row) for row in grade]
    result = []
    for l in range(1, n+1):
        result.append([grade_sums[l], cnt[l], time[l], l])
    result = sorted(result, key = lambda x: (-x[0], x[1], x[2]))
    # print(result)
    #내 팀 등수 찾기
    for l in range(n):
        if result[l][3] == t:
            print(l+1)
            break

#최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높다.
#최종 점수도 같고 제출 횟수도 같은 경우, 마지막 제출 시간이 더 빠른 팀의 순위가 높다.