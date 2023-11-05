n = int(input())
number = list(map(int,input().split()))
stack = []; ans = [-1]*len(number)
for idx, num in enumerate(number):
    while stack and stack[-1][1] < num:
        tmp = stack.pop()
        ans[tmp[0]] = num
    stack.append((idx, num))
print(*ans[:])