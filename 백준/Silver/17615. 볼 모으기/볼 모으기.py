import sys
input = sys.stdin.readline
N = int(input())
ball = input()

#R을 왼쪽으로 다 모을 때
flag = False
cnt1 = 0
for i in range(N):
    if ball[i] == 'B':
        flag = True
    elif flag and ball[i] == 'R':
        cnt1 +=1

#R을 오른쪽으로 다 모을 때
flag = False
cnt2 = 0
for i in range(N-1, -1, -1):
    if ball[i] == 'B':
        flag = True
    elif flag and ball[i] == 'R':
        cnt2 +=1
#B을 왼쪽으로 다 모을 때
flag = False
cnt3 = 0
for i in range(N):
    if ball[i] == 'R':
        flag = True
    elif flag and ball[i] == 'B':
        cnt3 +=1
#B을 왼쪽으로 다 모을 때
flag = False
cnt4 = 0
for i in range(N-1, -1, -1):
    if ball[i] == 'R':
        flag = True
    elif flag and ball[i] == 'B':
        cnt4 +=1

print(min(cnt1, cnt2, cnt3, cnt4))