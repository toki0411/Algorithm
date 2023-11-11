n = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))
def dfs(depth, plus, minus, multiply, divide, val):
    global max_val, min_val
    if depth == n:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return
    if plus:
        dfs(depth + 1, plus - 1, minus, multiply, divide, val + num[depth])
    if minus:
        dfs(depth + 1, plus, minus - 1, multiply, divide, val - num[depth])
    if multiply:
        dfs(depth + 1, plus, minus, multiply - 1, divide, val * num[depth])
    if divide:
        dfs(depth + 1, plus, minus, multiply, divide - 1, int(val / num[depth]))

max_val = -1e9; min_val = 1e9
dfs(1, operator[0], operator[1], operator[2], operator[3], num[0])
print(int(max_val))
print(int(min_val))
