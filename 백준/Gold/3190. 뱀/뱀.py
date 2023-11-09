from collections import deque
n = int(input())
apple_n = int(input())
apple = [list(map(int, input().split())) for _ in range(apple_n)]
snake_n = int(input())
snake = [list(input().split()) for _ in range(snake_n)]
direction = [[-1,0], [0,1], [1,0], [0,-1]] #북, 동, 남, 서

map = [[0] * n for _ in range(n)]  # 4는 사과, 1은 뱀
for i in range(len(apple)):
    ax, ay = apple[i][0], apple[i][1]
    map[ax-1][ay-1] = 4

dir = 1; snake_length = 1  # 뱀길이
q = deque([(0, 0)])
time = 0; x = y = 0
while q:
    x = x + direction[dir][0]
    y = y + direction[dir][1]
    time += 1
    #자기 머리나 벽인지, 사과인지 체크
    if 0<= x < n and 0<= y < n and (map[x][y] == 0 or map[x][y] == 4):
        if map[x][y] == 4:  #사과
            map[x][y] = 1
            q.append([x, y])
        else:
            map[x][y] = 1
            q.append([x, y])
            prev_x, prev_y = q.popleft()
            map[prev_x][prev_y] = 0
        # direction 변경
        if len(snake) > 0 and int(snake[0][0]) == time:
            if snake[0][1] == 'D':  # 오른쪽
                dir += 1
                if dir > 3:
                    dir = 0
            elif snake[0][1] == 'L':  # 왼쪽
                dir -= 1
                if dir < 0:
                    dir = 3
            del snake[0]
    else:

        print(time)
        break

