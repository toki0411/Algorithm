n = int(input())
voca = [input() for _ in range(n)]; dict = {}
for i in range(len(voca)):
    x = len(voca[i])-1
    for j in range(len(voca[i])):
        if voca[i][j] in dict:
            dict[voca[i][j]] += 10**x
        else:
            dict[voca[i][j]] = 10**x
        x -= 1
word = sorted(dict.values(), reverse=True)
num = 9; ans =0
for i in range(len(word)):
    ans += num * word[i]
    num -= 1

print(ans)


