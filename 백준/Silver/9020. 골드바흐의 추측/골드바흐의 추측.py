n = int(input())
sosu = [i for i in range(10001)]
for i in range(2, 10001):
    for j in range(i + i, 10001, i):
        if sosu[j] != 0:
            sosu[j] = 0

for _ in range(n):
    x = int(input())
    a=b = 0
    if x % 2 == 0:
        a = x // 2
        b = x // 2
    else:
        a = x//2
        b = x//2 + 1
    while True:
        if sosu[a] != 0 and sosu[b] != 0:
            print(sosu[a], sosu[b])
            break
        else:
            a-=1; b += 1


