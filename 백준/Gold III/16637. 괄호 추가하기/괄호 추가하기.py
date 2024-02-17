import sys

def calculate(opIdx):
    cnt = 0
    exp = []
    for i in range(len(expression)):
        exp.append(expression[i])
    for op in opIdx:
        idx = op - cnt
        exp[idx - 1] = str(eval(exp[idx - 1] + exp[idx] + exp[idx + 1]))
        del exp[idx:idx + 2]
        cnt += 2
    cnt = 0

    for i in range(1, len(exp) - 1, 2):
        idx = i - cnt
        exp[idx - 1] = str(eval(exp[idx - 1] + exp[idx] + exp[idx + 1]))
        del exp[idx:idx + 2]
        cnt += 2

    return int(exp[0])


def dfs(idx, opIdx):
    # print(idx, opIdx)
    global ans
    if idx == n - 2:
        ans = max(calculate(opIdx), ans)
        return

    for i in range(idx + 2, n - 1, 2):
        if idx in opIdx:  # 이전에 괄호 사용
            dfs(i, opIdx)
        else:  # 이전에 괄호 사용하지 않았음
            dfs(i, opIdx + [i])
            dfs(i, opIdx)


n = int(sys.stdin.readline())
expression = list(sys.stdin.readline().rstrip())
ans = -(1e8)
opIdx = []
dfs(-1, opIdx)
print(ans)
