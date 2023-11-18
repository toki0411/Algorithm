n = int(input())
str = list(input())
num = [int(input()) for _ in range(n)]
s = []
for i in range(len(str)):
    if str[i].isalpha():
        s.append(num[ord(str[i]) - ord('A')])
    else:
        a = s.pop()
        result = s.pop()
        if str[i] == '*':
            result *= a
        elif str[i] == '/':
            result /= a
        elif str[i] == '-':
            result -= a
        elif str[i] == '+':
            result += a

        s.append(result)
print('%.2f' %s[-1])
