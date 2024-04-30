import sys

input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
crane.sort()
box.sort()
ans = 0
if box[-1] > crane[-1]:
    ans = -1
else:
    while len(box) > 0:
        for i in range(len(crane) - 1, -1, -1):
            if box and crane[i] - box[0] < 0:
                break
            for j in range(len(box) - 1, -1, -1):
                if crane[i] >= box[j]:
                    del box[j]
                    break
        ans += 1
print(ans)