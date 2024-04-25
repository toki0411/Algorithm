n = int(input())
ans = 1e9
arr = [[0] * (n) for _ in range(6)]
for i in range(n):
    a, b = map(int, input().split())
    ans = min(a, b, ans)
    arr[a][i] = 1
    arr[b][i] = 1

student_num = 1

for i in range(1,6):
    cnt = 1
    for j in range(n-1):
        if arr[i][j] == arr[i][j+1] == 1 :
            cnt += 1
        else:
            cnt = 1
        if cnt > student_num:
            student_num = cnt
            ans = i
print(student_num, ans)