def findParents(x):
    if x in a:
        return x
    # parents[x] = findParents(parents[x])
    return parents[x]
    # if x in a:
    #     return x
    # else:
    #     return 0


def union(x, y):
    xRoot = findParents(x)
    yRoot = findParents(y)
    if xRoot != 0 and yRoot == 0:
        parents[y] = xRoot
        parents[x] = xRoot
        return True
    elif xRoot == 0 and yRoot != 0:
        parents[x] = yRoot
        parents[y] = yRoot
        return True
    # elif xRoot != 0 and yRoot != 0:
    #
    # else: #둘다 0
    #     return True


N, M = map(int, input().split())
parents = [0] * (N + 1)
cnt = 0
a = list(map(int, input().split()))
for i in range(1, a[0] + 1):
    x = a[i]
    parents[x] = x
party = []
a.pop(0)
for i in range(M):
    p = list(map(int, input().split()))
    party.append(p[1:])
flag = True
while flag:
    flag = False
    for i in range(M):
        p = party[i]
        # union
        for j in range(len(p) - 1):
            for l in range(j + 1, len(p)):
                key = union(p[j], p[l])
                if key:
                    flag = True
# for i in range(M - 1, -1, -1):
#     p = party[i]
#     # union
#     for j in range(len(p) - 1):
#         for l in range(j + 1, len(p)):
#             union(p[j], p[l])
    # for j in range(len(p)-1, 1, -1):
    #     for l in range(j-1, 0, -1):
    #         print(i, j, l)
    #         union(p[j], p[l])
    # 하나짜리면 union생략 후 findparents
# print(parents)
for i in range(M):
    p = party[i]
    key = True
    for j in range(len(p)):
        if parents[p[j]] != 0:
            key = False
            break
    if key:
        cnt += 1
print(cnt)