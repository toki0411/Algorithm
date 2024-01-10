s = input()
duck = ["q", 'u', 'a', 'c', 'k']
cnt = 0
key = False
while True:
    if len(s) % 5 != 0 or len(s) == 0:
        break
    if 'q' in s and 'u' in s and 'a' in s and 'c' in s and 'k' in s:
        idx = 0
    else:
        key = True
        break

    tmp = []
    for i in range(len(s)):
        if s[i] == duck[idx]:
            idx += 1
            if idx > 4:
                idx = 0
        else:
            tmp.append(s[i])
    s = ''.join(tmp)
    if idx == 0:
        cnt += 1
if 0 < len(s) and (len(s) % 5) != 0:
    cnt = -1
if key:
    cnt = -1
print(cnt)
