from collections import deque

n, w, k = map(int, input().split())
truck = list(map(int, input().split()))
t = 0
b = [0] * w
while b:
    t +=1
    b.pop(0)
    if truck:
        if sum(b) + truck[0] <= k:
            b.append(truck[0])
            truck.pop(0)
        else:
            b.append(0)
print(t)