n = int(input())
arr = [int(input()) for _ in range(n)]
s = [1]; idx = 2; ans = ['+']
for i in range(n):
    key = False
    while True:
        if not s and idx <= n:
            s.append(idx)
            ans.append('+')
            idx += 1
        elif s[-1] == arr[i]:
            s.pop()
            ans.append('-')
            break
        elif s[-1] < arr[i]:
            s.append(idx)
            ans.append('+')
            idx += 1
        else:
            key = True
            break
    if key:
        print("NO")
        exit(0)

for i in ans:
    print(i)
