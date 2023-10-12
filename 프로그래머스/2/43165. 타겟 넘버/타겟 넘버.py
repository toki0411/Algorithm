def dfs(numbers, target, depth, val):
    global cnt
    if depth == len(numbers):
        if val == target:
            cnt +=1
            return 
        else:
            return
    
    dfs(numbers, target, depth + 1, val + numbers[depth])
    dfs(numbers, target, depth + 1, val - numbers[depth])

def solution(numbers, target):
    global cnt
    cnt = 0
    dfs(numbers, target, 0, 0)
    return cnt