from itertools import combinations
t = int(input())
for tc in range(1, t+1):
    num = list(map(int, input().split()))
    com_arr = list(combinations(num, 3))
    com_arr.sort(key = lambda x: -sum(x))
    ans = idx = 0
    for i in range(len(com_arr)):
        if sum(com_arr[i]) != ans:
            idx += 1
            ans = sum(com_arr[i])
            if idx == 5:
                break
    print('#{} {}'.format(tc, ans))