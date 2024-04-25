d = [1,5,10,50]
def dfs(depth, number, start):
    if depth == N:
        num.add(number)
        return
    for i in range(start, 4):
        dfs(depth + 1, number + d[i], i)

N = int(input())
if N == 1:
    print(4)
else:
    num = set()
    dfs(0,0, 0)
    print(len(num))