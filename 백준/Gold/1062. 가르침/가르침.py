import sys

N,K = map(int,sys.stdin.readline().split())
set_word = []
for i in range(N):
    word_input = sys.stdin.readline().rstrip()
    set_word.append(set(list(word_input)))

learn = [0]*26
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1

answer = 0

def dfs(idx, cnt):
    global answer
    if cnt == K - 5:
        readcnt = 0
        for word in set_word:
            flag = True
            for w in word:
                if learn[ord(w) - ord('a')] == 0:
                    flag = False
                    break;
            if flag:
                readcnt += 1
        answer = max(answer, readcnt)
        return
    
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = 1
            dfs(i+1, cnt + 1)
            learn[i] = 0
            

if K<5:
    print(0)
elif K==26:
    print(N)
else:
    dfs(0,0)
    print(answer)