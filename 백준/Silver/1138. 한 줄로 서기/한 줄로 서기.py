n = int(input())
line = list(map(int, input().split()))
arr = [0] * (n)
for i in range(1, n+1):  #키 1, 2, 3, 4
    for j in range(n):
        if arr[j] == 0:
            before = 0
            for k in range(j):
                if arr[k] == 0:
                    before+=1
            if before == line[i-1]:
                arr[j] = i
                break
print(*arr[::])
