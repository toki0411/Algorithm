def dfs(s, start, cnt, k):
    global idx
    if cnt == k:
        idx += 1
        ans.append(int(''.join(s)))
        return

    for i in range(start, 10):
        dfs(s + num[i], i + 1, cnt + 1, k)
N = int(input())
num = ['9','8','7','6','5','4','3','2','1','0']
if N < 10:
    print(N)
    exit()
elif N >= 1023:
    print(-1)
    exit()
ans = [0,1,2,3,4,5,6,7,8,9]
idx = 9
for i in range(2, 12):
    dfs("", 0, 0, i)
    if N <= idx:
        ans.sort()
        break
print(ans[N])