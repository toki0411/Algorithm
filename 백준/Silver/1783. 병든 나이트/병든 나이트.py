n, m = map(int, input().split())
if n == 1:
    print(1)
elif n == 2:
    if m >= 1 and m <= 6:  # m이 1~6일 때
        print((m + 1) // 2)
    elif m >= 7:
        print(4)
elif m <= 6:
    print(min(m, 4))
else:
    print(m-2)

