t = int(input())
for tc in range(1, t+1):
    tt = int(input())
    number = list(map(int, input().split()))
    dict = {}
    for num in number:
        if num in dict:
            dict[num]+=1
        else:
            dict[num] = 1
    ans = sorted(dict.items(), reverse=True)
    ans.sort(key = lambda x:-x[1])

    print('#{} {}'.format(tt, ans[0][0]))