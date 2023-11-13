

for tc in range(1, 11):
    str =list(input().split())
    n = int(str[0])
    str = list(str[1])
    s = []
    for i in range(len(str)):
        if not s:
            s.append(str[i])
        else:
            if s[-1] == str[i]:
                s.pop()
            else:
                s.append(str[i])


    print('#{} {}'.format(tc, ''.join(s)))