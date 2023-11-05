n, k = map(int, input().split())
number = list(map(str,input()))
ans = []; limit = len(number)-k
for num in number:
    while ans and k>0 and ans[-1] < num:
        ans.pop()
        k-=1
    ans.append(num)
print(''.join(ans[:limit]))
