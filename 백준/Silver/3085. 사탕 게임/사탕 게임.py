n = int(input())
graph = [list(input()) for _ in range(n)]

def check(arr):
    n = len(arr)
    answer = 1
    for i in range(n):
        # 열 순회하면서 연속되는 숫자 세기
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                # 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
                # 이전과 다르다면 다시 1로 초기화
                cnt = 1

            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt

        # 행 순회하면서 연속되는 숫자 세기
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                # 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
                # 이전과 다르다면 다시 1로 초기화
                cnt = 1

            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt

    return answer
ans = 0
for i in range(n):
    for j in range(n):
        if j+1 < n:
            # 옆의 것과 교환(색 다를 경우에만)
            graph[i][j], graph[i][j+1]  = graph[i][j+1], graph[i][j]
            #행과 열 체크
            tmp = check(graph)
            if tmp > ans:
                ans = tmp
            # 다시 교환
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
        if i+1 < n:
            # 아래것과 교환 (색 다를 경우에만)
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
            #행과 열 체크
            tmp = check(graph)
            if tmp > ans:
                ans=tmp
            # 다시 교환
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
print(ans)