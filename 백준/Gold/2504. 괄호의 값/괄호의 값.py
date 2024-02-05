str = list(input())
result = 0
res = 1
s = []
for i in range(len(str)):
    if str[i] == '(':
        res *= 2
        s.append('(')

    elif str[i] == '[':
        res *= 3
        s.append('[')

    elif str[i] == ')':
        if not s or s[-1] != '(':
            result = 0
            break
        if str[i - 1] == '(':
            result += res
        res //= 2
        s.pop()

    elif str[i] == ']':
        if not s or s[-1] != '[':
            result = 0
            break
        if str[i - 1] == '[':
            result += res
        res //= 3
        s.pop()

if s:
    print(0)
else:
    print(result)