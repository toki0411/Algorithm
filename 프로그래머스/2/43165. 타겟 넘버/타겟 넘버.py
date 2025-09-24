def dfs(cnt, target, limit, cmd, numbers):
    global answer
    if cnt == limit : 
        if cal(cmd, numbers) == target:
            answer += 1
        return 
    dfs(cnt + 1, target, limit, cmd + ['+'], numbers)
    dfs(cnt + 1, target, limit, cmd + ['-'], numbers)
def cal(cmd, numbers) :
    val = 0
    for i in range(len(cmd)):
        if cmd[i] == '+':
            val += numbers[i] 
        else:
            val -= numbers[i]     
    return val
def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, target, len(numbers) , [], numbers)
    return answer