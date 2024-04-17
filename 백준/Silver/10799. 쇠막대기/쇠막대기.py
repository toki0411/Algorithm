list = list(input())
s = []
cnt = 0
i = 0
while i < len(list):
    if list[i] == '(':
        if i + 1 < len(list) and list[i + 1] == ')':  # 레이저
            cnt += len(s)
            i += 1
        else:
            s.append(i)
    else:
        cnt += 1
        s.pop()

    i += 1

print(cnt)