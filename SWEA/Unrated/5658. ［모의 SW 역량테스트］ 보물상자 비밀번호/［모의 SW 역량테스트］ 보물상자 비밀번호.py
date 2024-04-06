T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    box = list(input())
    pw = set()

    for k in range(1000):
        key = False
        for i in range(0, N, N // 4):
            s = ''.join(box[i:i+N//4])
            val = int(s, 16)
            if val not in pw:
                pw.add(val)
                key = True
        box.insert(0, box[-1])
        box.pop()
        if not key:
            break
    pw = list(pw)
    pw.sort(key = lambda x: -x)

    print("#{} {}".format(tc, pw[K-1]))
