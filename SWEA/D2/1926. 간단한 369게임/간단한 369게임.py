n = int(input())

for i in range(1,n+1):
    num = str(i)
    ans = []
    for j in range(len(num)):
        if num[j] in ["3", "6", "9"]:
            ans.append('-')
    if ans:
        print(''.join(ans), end = " ")
    else:
        print(i, end = " ")
