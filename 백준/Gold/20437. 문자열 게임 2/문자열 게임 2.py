T = int(input())

for _ in range(T):
    s = input()
    k = int(input())
    idx = [[] for _ in range(26)]
    for i in range(len(s)):
        idx[ord(s[i])-97].append(i)
    minlen = len(s)
    maxlen = -1
    for i in range(len(idx)):
        for j in range(len(idx[i])-k + 1):
            minlen = min(minlen, abs(idx[i][j]-idx[i][j+k-1])+1 )
            maxlen = max(maxlen, abs(idx[i][j]-idx[i][j+k-1])+1)
    if minlen == len(s) and maxlen == -1:
        print(-1)
    else:
        print(minlen, maxlen)