n, k = map(int, input().split())
list = list(map(int, input().split()))
diff = []
for i in range(1, n):
    diff.append(list[i] -list[i-1])
diff.sort(key = lambda x: -x)
print(sum(diff[k-1:]))