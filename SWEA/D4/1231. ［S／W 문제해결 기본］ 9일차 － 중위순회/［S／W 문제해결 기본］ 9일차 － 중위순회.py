def inorder(x):
    global ans
    if x != '.':
        inorder(tree[x][0])
        ans.append(dict[x])
        inorder(tree[x][1])

for tc in range(1, 11):
    n = int(input())
    tree = {}; dict = {}
    for l in range(n):
        tmp = list(input().split())
        root = int(tmp[0])
        word = tmp[1]; left = right = '.'
        if len(tmp) == 4:
            left, right = int(tmp[2]), int(tmp[3])
        elif len(tmp) == 3:
            left = int(tmp[2])
        tree[root] = [left, right]
        dict[root] = word
    ans = []
    inorder(1)

    print('#{} {}'.format(tc, ''.join(ans)))



