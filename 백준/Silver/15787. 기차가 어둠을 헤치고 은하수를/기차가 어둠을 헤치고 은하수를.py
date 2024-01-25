from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
command = [list(map(int, input().split())) for _ in range(m)]
train = [0] * n
for j in range(m):
    if command[j][0] ==1:
        i, x = command[j][1]-1, command[j][2]-1
        train[i] = train[i] | 1 << x  #x번째 bit를 or연산하면 x번째에 승객을 (+1) 태운것과 같아짐
    elif command[j][0] == 2:
        i, x = command[j][1]-1, command[j][2]-1
        train[i] = train[i] & ~(1 << x) #x번째 승객만 0이므로 and 연산 시, x번째 승객만 하차
    elif command[j][0] == 3: # 뒤로 (비트 오른쪽 연산)
        i = command[j][1]-1
        train[i] = train[i] << 1
        train[i] = train[i] & ~(1 << 20) #20번째 승객은 하차
    elif command[j][0] == 4:  # 앞으로 (비트 왼쪽 연산)
        i = command[j][1]-1
        train[i] = train[i] >> 1

print(len(set(train)))

