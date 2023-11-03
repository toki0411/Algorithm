n = int(input())
def dfs(left, eggs):
    global ans
    if left == n:
        cnt =0
        for i in range(n):
            if eggs[i] <= 0 :
                cnt += 1
        if cnt > ans:
            ans = cnt
        return
    if eggs[left] > 0:
        for i in range(n):
            flag = False
            if eggs[i] > 0 and i != left:
                flag = True
                tmp = eggs[left]; tmp2 = eggs[i]
                eggs[left] -= w[i]
                eggs[i] -= w[left]
                dfs(left+1, eggs)
                eggs[left] = tmp
                eggs[i] = tmp2
        if not flag:
            dfs(left+1, eggs)
    # 왼쪽 손의 계란이 깨져있음
    else:
        dfs(left+1, eggs)

s = [0] * n
w = [0] * n
for i in range(n):
    s[i], w[i] = map(int, input().split())
ans = 0
dfs(0, s)
print(ans)
