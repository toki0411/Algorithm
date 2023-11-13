t = int(input())
for tc in range(1, t+1):
    n,m,k = map(int,input().split())
    people = list(map(int, input().split()))
    people.sort()
    time = 0; bread = 0; key = False
    for i in range(len(people)):
        if (int(people[i] / m)*k - i) <= 0:
            key = True
            break
    if key :
        ans = "Impossible"
    else:
        ans = "Possible"
    print('#{} {}'.format(tc, ans))

