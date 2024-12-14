n = int(input())
k = int(input())
arr = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
arr[(n-1) // 2][(n-1) // 2] = 1
nx , ny = (n-1) // 2 - 1, (n-1) // 2
cnt = 3
num = 2
ans_x = (n-1) // 2 
ans_y = (n-1) // 2
while cnt <= n:
    for i in range(4):
        for c in range(1, cnt):
            arr[nx][ny] = num
            if num == k :
                ans_x = nx
                ans_y = ny
            num += 1
            if c != (cnt - 1):
                nx += dx[i]
                ny += dy[i]
            elif c == cnt-1 and i+1 < 4:
                nx += dx[i+1]
                ny += dy[i+1]
            else:
                nx -= 1
    cnt += 2

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')

    print()
print(ans_x+1, ans_y+1, end ='')