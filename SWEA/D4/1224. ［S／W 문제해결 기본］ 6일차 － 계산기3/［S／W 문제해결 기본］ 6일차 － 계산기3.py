for tc in range(1, 11):
    n = list(input())
    str = input()
    s = []
    result = []
    for i in str:
        if i.isdigit():
            result.append(i)
        else:
            if i == '(':
                s.append(i)
            elif i == '*':
                while s and s[-1] == '*':
                    result.append(s.pop())
                s.append(i)
            elif i == '+':
                while s and s[-1] != '(':
                    result.append(s.pop())
                s.append(i)
            elif i == ')':
                while s and s[-1] != '(':
                    result.append(s.pop())
                s.pop()
    while s:
        result.append(s.pop())

    cal = []
    for i in result:
        if i == '+':
            a = cal.pop()
            b = cal.pop()
            cal.append(a + b)
        elif i == '*':
            a = cal.pop()
            b = cal.pop()
            cal.append(a * b)
        else:
            cal.append(int(i))
    print('#{} {}'.format(tc, cal.pop()))



