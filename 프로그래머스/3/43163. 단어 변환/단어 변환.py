def dfs(word, target, cnt, words):
    global answer, visited
    if word == target:
        answer = min(answer, cnt)
        return 
    if cnt > answer:
        return 
    for i in range(len(words)):
        if changeable(word, words[i]) and not visited[i]:
            visited[i] = 1
            dfs(words[i], target, cnt + 1, words)
            visited[i] = 0

            
def changeable(word, target):
    diff = 0
    for i in range(len(word)):
        if word[i] != target[i]:
            diff += 1
    if diff == 1:
        return True
    else:
        return False
        
def solution(begin, target, words):
    global answer, visited
    answer = 1e9
    if target not in words:
        return 0
    visited = [0] * len(words)
    dfs(begin, target, 0, words)
    
    return answer