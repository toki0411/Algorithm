def check(word, begin):
    cnt = 0
    for i in range(len(word)):
        if word[i] != begin[i]:
            cnt += 1
    if cnt == 1: return True
    else: return False
def solution(begin, target, words):
    visited = [0] * len(words)
    if target not in words:
        return 0

    def dfs(begin, ans, min_val):
        if begin == target:
            min_val = min(len(ans), min_val)
            return min_val
        for idx, word in enumerate(words):
            if not visited[idx] and check(word, begin):
                visited[idx] = 1
                min_val = dfs(word, ans + [word], min_val)
                visited[idx] = 0
        return min_val
    return dfs(begin, [], len(words))