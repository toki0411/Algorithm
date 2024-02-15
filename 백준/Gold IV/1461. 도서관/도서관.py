n, m = map(int, input().split())
input = list(map(int, input().split()))
negBook = [];
posBook = []
ans = 0
for i in range(len(input)):
    if input[i] < 0:
        negBook.append(input[i])
    elif input[i] > 0:
        posBook.append(input[i])

negBook.sort(key=lambda x: -x);
posBook.sort()
key = False;

if m >= (len(negBook) + len(posBook)):
    c = 0;
    d = 0
    if len(negBook) > 0: c = abs(negBook[-1])
    if len(posBook) > 0: d = posBook[-1]
    if c != 0 and d != 0:
        if c > d:
            ans += c
            ans += d * 2
        else:
            ans += d
            ans += c * 2
    elif c != 0 or d != 0:
        if c != 0:
            ans += c
        else:
            ans += d

    print(ans)
    exit(0)
a = 0;
b = 0;
if len(negBook) > 0: a = abs(negBook[-1])
if len(posBook) > 0: b = posBook[-1]

cnt = 0;
tmp = 0;
if a > b:
    tmp = abs(negBook[-1])
    for i in range(len(negBook) - 1, -1, -1):
        if cnt == m :
            cnt = 0
            if key:
                ans += (tmp * 2)
            else:
                key = True;
                ans += tmp
            tmp = 0

        tmp = max(abs(negBook[i]), tmp)
        cnt += 1
    if key:
        ans += (tmp * 2)
    else:
        ans += tmp

    cnt = 0;
    if len(posBook) > 0:
        tmp = posBook[-1]
        for i in range(len(posBook) - 1, -1, -1):
            if cnt == m:
                cnt = 0
                ans += (tmp * 2)
                tmp = 0

            tmp = max(posBook[i], tmp)
            cnt += 1
        ans += (tmp * 2)

elif a <= b:
    tmp = posBook[-1]
    for i in range(len(posBook) - 1, -1, -1):
        if cnt == m:
            cnt = 0
            if key:
                ans += (tmp * 2)
            else:
                key = True;
                ans += tmp
            tmp = 0

        tmp = max(posBook[i], tmp)
        cnt += 1
    if key:
        ans += (tmp * 2)
    else:
        ans += tmp

    cnt = 0;
    if len(negBook) > 0:
        tmp = abs(negBook[-1])
        for i in range(len(negBook) - 1, -1, -1):
            if cnt == m:
                cnt = 0
                ans += (tmp * 2)
                tmp = 0

            tmp = max(abs(negBook[i]), tmp)
            cnt += 1

        ans += (tmp * 2)

print(ans)