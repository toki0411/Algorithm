n,  m = map(int, input().split())
dic1 = dict()
dic2 = dict()
for i in range(1,n+1):
    s = input()
    dic1[i] = s
    dic2[s] = i

for i in range(m):
    s = input()
    if s.isdigit():
        print(dic1[int(s)])
    else:
        print(dic2[s])