def check(wallet, bill):
    if wallet[0] >= bill[0]:
        if wallet[1] >= bill[1]:
            return True
    if wallet[0] >= bill[1]:
        if wallet[1] >= bill[0]:
            return True
    return False


def dfs(wallet, bill, ans):
    global answer
    if check(wallet, bill):
        answer = ans
        return
    if bill[0] > bill[1]:
        bill[0] = bill[0] // 2
        dfs(wallet, bill, ans + 1)
    else:
        bill[1] = bill[1] // 2
        dfs(wallet, bill, ans + 1)


answer = 0
def solution(wallet, bill):
    global answer
    dfs(wallet, bill, 0)
    return answer

