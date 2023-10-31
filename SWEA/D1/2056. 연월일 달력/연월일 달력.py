t = int(input())
for t_ in range(1, t + 1):
    arr = input()
    year = arr[:4]
    month = arr[4:6]
    day = arr[6:]
    key = True; ans = None
    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if 1<= int(day) <= 31:
            ans = year+ "/"+ month+ "/" + day
        else:
            key = False
    elif int(month) in [4, 6, 9, 11]:
        if 1 <= int(day) <= 30:
            ans = year+ "/" + month+ "/" + day
        else:
            key = False
    elif int(month) == 2 : # 2월
        if 1 <= int(day) <= 28:
            ans = year+ "/" + month+ "/" + day
        else:
            key = False
    else:
        key = False

    if not key:
        ans = -1
    print('#{} {}'.format(t_, ans))