T = int(input())
for tc in range(T):
    n = int(input())
    othello = list(input())
    goal = list(input())
    arr = []
    for i in range(n):
        if othello[i] != goal[i]:
            arr.append(othello[i])

    if arr.count('B') == arr.count('W'):
        print(arr.count('B'))
    elif arr.count('B') > arr.count('W'):
        print(arr.count('B'))
    elif arr.count('B') < arr.count('W'):
        print(arr.count('W'))