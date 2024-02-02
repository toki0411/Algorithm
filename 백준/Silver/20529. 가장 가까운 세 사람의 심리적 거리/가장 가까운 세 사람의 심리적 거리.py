T = int(input())

def dfs(cnt, start):
    global ans
    if cnt == 3:
        val = 0
        a = student[tmp[0]]
        b = student[tmp[1]]
        c = student[tmp[2]]

        # a - b
        if a != b:
            for i in range(4):
                if a[i] != b[i]:
                    val += 1
        # a - c
        if a != c:
            for i in range(4):
                if a[i] != c[i]:
                    val += 1
        # b - c
        if b != c:
            for i in range(4):
                if b[i] != c[i]:
                    val += 1

        ans = min(ans, val)
        return

    for i in range(start, N):
        tmp[cnt] = i
        dfs(cnt + 1, i + 1)

for t in range(T):
    N = int(input())
    student = list(input().split())
    ans = 1000000
    tmp = [0, 0, 0]
    if N <= 32:
        dfs(0, 0)
        print(ans)
    else:
        print(0)