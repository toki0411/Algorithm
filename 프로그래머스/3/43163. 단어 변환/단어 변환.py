answer = 1e9
def dfs(begin, target, words, cnt, visited):  #백트래킹
    global answer 
    if begin == target:
        answer = min(cnt, answer)
        return 
    for i in range(len(words)):
        if not visited[i]:
            if changeable(begin, words[i]):
                visited[i] = 1
                dfs(words[i], target, words, cnt + 1, visited)
                visited[i] = 0

#변경할 수 있는 단어인지 확인                 
def changeable(begin, target):
    diffCnt = 0 
    for i in range(len(begin)):
        if begin[i] != target[i]:
            diffCnt +=1
    
    if diffCnt == 1:
        return True
    else:
        return False
    
def solution(begin, target, words):
    visited = [0] * len(words)
    dfs(begin, target, words, 0, visited)
    if answer == 1e9 : return 0
    else : return answer