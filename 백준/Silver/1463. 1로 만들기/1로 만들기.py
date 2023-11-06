N = int(input())
d = [0] * (N+1)

if(N < 4) :
    arr = [0] * 4
    arr[1] = 0
    arr[2] = 1
    arr[3] = 1
    print(arr[N])
else:
    d[1] = 0
    d[2] = 1
    d[3] = 1
    for i in range(4, N+1):
        two = 1 + d[i // 2] + i%2
        three = 1 + d[i // 3] + i%3
        if(two > three):
            d[i] = three
        elif (two <= three):
            d[i] = two

    print(d[N])