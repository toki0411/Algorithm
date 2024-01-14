t = int(input())
for t_ in range(1, t + 1):
    int(input())
    dict = {}
    arr = list(map(int, input().split()))
    for num in arr:
        if dict.get(num):
            dict[num] += 1
        else:
            dict[num] = 1

    sorted_dict = sorted(dict.items(), key = lambda item: -item[1])
    print('#{} {}'.format(t_, sorted_dict[0][0]))