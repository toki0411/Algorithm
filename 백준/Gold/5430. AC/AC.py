T = int(input())
for t in range(T):
    cmd = list(input())
    n = int(input())
    num = list(input().split(','))
    num[0] = num[0][1:]
    num[-1] = num[-1][:len(num[-1])-1]

    for i in range(n):
        num[i] = int(num[i])
    errorCheck = False
    if num[0] == num[-1] == '':
        del num[0]
    reverse = False
    for c in cmd:
        if c == 'R':
            if reverse == False:
                reverse = True
            else:
                reverse = False
        else:
            if len(num) > 0:
                if reverse:
                    del num[-1]
                else:
                    del num[0]
            else:
                print("error")
                errorCheck = True
                break
    if not errorCheck:
        print('[', end='')
        if not reverse:
            for i in range(len(num)):
                print(num[i], end='')
                if i != len(num)-1:
                    print(',', end = '')
        else:
            num = num[::-1]
            for i in range(len(num)):
                print(num[i], end='')
                if i != len(num)-1:
                    print(',', end = '')
        print(']')