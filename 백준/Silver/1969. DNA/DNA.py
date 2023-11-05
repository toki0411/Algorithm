N, M = map(int, input().split())
str = []
for i in range(N):
    s = input()
    str.append(s)
ans = ''
sum = 0
for i in range(M):
    d = {}
    for j in range(N):
        if str[j][i] in d:
            d[str[j][i]] +=1

        else :
            d[str[j][i]]= 1
        sum += 1

    d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    sum-=d[0][1]
    ans+=d[0][0]

print(ans)
print(sum)