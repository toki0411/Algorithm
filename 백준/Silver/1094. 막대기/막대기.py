x = int(input())

stick = [64]

while True:
    total = sum(stick)
    if total == x:
        break
    elif total > x:
        half = stick[0] // 2
        stick[0] = half
        if sum(stick) < x:
            stick.append(half)

    stick.sort()

print(len(stick))