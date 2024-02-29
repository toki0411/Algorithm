def check(line):
    visited = [0] * n
    for i in range(1, n):
        if abs(line[i - 1] - line[i]) > 1:
            return False
        if line[i - 1] < line[i]:  # 현재값이 큼
            for j in range(i - 1, i - L-1, -1):  # 왼쪽에 경사로 설치
                if j < 0 or visited[j] or line[i - 1] != line[j]:
                    return False
                visited[j] = 1

        elif line[i - 1] > line[i]:  # 현재값이 작음
            for j in range(i, i + L):  # 오른쪽에 경사로 설치
                if j >= n or visited[j] or line[i] != line[j]:
                    return False
                visited[j] = 1
    # print(line)
    return True


n, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
reversed_graph = graph[::-1]
rotated = list(zip(*reversed_graph))
cnt = 0
for line in graph:
    if check(line): cnt += 1
for line in rotated:
    if check(line): cnt += 1
print(cnt)