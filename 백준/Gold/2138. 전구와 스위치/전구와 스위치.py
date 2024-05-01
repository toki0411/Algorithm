import copy


def switch(b):
    if b == 0:
        return 1
    else:
        return 0


def check(bulb):
    for i in range(n):
        if bulb[i] != goal[i]:
            return False
    return True


n = int(input())
bulb_list = list(map(int, input()))
bulb = copy.deepcopy(bulb_list)
goal = list(map(int, input()))
ans = 1e9

# 0번째 누름
cnt = 1
bulb[0] = switch(bulb[0])
bulb[1] = switch(bulb[1])
for i in range(1, n):
    if i == n - 1 and goal[i - 1] != bulb[i - 1]:  # 젤 끝
        cnt += 1
        bulb[i - 1] = switch(bulb[i - 1])
        bulb[i] = switch(bulb[i])
    elif goal[i - 1] != bulb[i - 1]:  # i-1 인덱스의 전구를 눌러야 하는지 체크
        cnt += 1
        bulb[i - 1] = switch(bulb[i - 1])
        bulb[i] = switch(bulb[i])
        bulb[i + 1] = switch(bulb[i + 1])
if check(bulb):
    ans = min(ans, cnt)

cnt = 0
# 모든 전구들이 goal이랑 같아졌는지 체크
bulb = copy.deepcopy(bulb_list)
# 0번째 누르지 않음
for i in range(1, n):
    if i == n - 1 and goal[i - 1] != bulb[i - 1]:  # 젤 끝
        cnt += 1
        bulb[i - 1] = switch(bulb[i - 1])
        bulb[i] = switch(bulb[i])
    elif goal[i - 1] != bulb[i - 1]:  # i-1 인덱스의 전구를 눌러야 하는지 체크
        cnt += 1
        bulb[i - 1] = switch(bulb[i - 1])
        bulb[i] = switch(bulb[i])
        bulb[i + 1] = switch(bulb[i + 1])
if check(bulb):
    ans = min(ans, cnt)

if ans == 1e9:
    print(-1)
else:
    print(ans)