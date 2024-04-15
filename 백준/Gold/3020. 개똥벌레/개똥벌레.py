import sys
sys.stdin.readline
N, H = map(int, input().split())  #길이, 높이
down = [0] * (H+1)
up = [0] * (H+1)
minCnt = 1e8
cnt = 0
for i in range(N):
    h = int(input())
    if i % 2 == 0:
        down[h] += 1
    else:
        up[h] += 1

for i in range(H, 0, -1):
    if down[i]:
        down[i-1] += down[i]
    if up[i]:
        up[i-1] += up[i]

for i in range(1, H+1):
    if down[i] + up[H-i + 1] < minCnt:
        minCnt = down[i] + up[H-i+1]
        cnt = 1
    elif down[i] + up[H-i +1] == minCnt:
        cnt += 1

print(minCnt, cnt)
#[0, 7, 6, 5, 1, 0] [0, 7, 7, 5, 2, 0]