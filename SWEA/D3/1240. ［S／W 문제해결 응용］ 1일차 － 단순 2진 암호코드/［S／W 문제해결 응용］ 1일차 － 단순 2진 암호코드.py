t = int(input())
def findNum(c):
    num_range = []; cnt = 1
    for i in range(len(c)-1):
        if c[i] != c[i+1]:
            num_range.append(cnt)
            cnt = 0
        cnt += 1
    num_range.append(cnt)
    if num_range == [3,2,1,1]:
        return 0
    if num_range == [2,2,2,1]:
        return 1
    if num_range == [2,1,2,2]:
        return 2
    if num_range == [1,4,1,1]:
        return 3
    if num_range == [1,1,3,2]:
        return 4
    if num_range == [1,2,3,1]:
        return 5
    if num_range == [1,1,1,4]:
        return 6
    if num_range == [1,3,1,2]:
        return 7
    if num_range == [1,2,1,3]:
        return 8
    if num_range == [3,1,1,2]:
        return 9
for tc in range(1, t+1):
    ans = 0
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]
    code = []
    for i in range(n):
        if sum(arr[i]) != 0:
            idx = 0
            for j in range(len(arr[i])):
                if arr[i][j] == 1:
                    idx = j

            for l in range(idx, idx - 56, -7):
                code.append(arr[i][l-6:l+1])
            break
    code = [0] + code[::-1]; num1 = num2 = 0
    for i in range(1, len(code)):
        num = findNum(code[i])
        ans += num
        #홀수
        if i % 2 == 1:
            num1 += num
        #짝수
        else:
            num2 += num
    if (num1 * 3 + num2 ) % 10 == 0:
        print('#{} {}'.format(tc, ans))
    else:
        print('#{} {}'.format(tc, 0))
