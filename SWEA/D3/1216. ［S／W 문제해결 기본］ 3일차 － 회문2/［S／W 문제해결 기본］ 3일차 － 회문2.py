
for tc in range(1, 11):
    t = int(input())
    graph = [list(input()) for _ in range(100)]
    ans = 0
    for i in range(100):
        for j in range(100):
            #가로
            for k in range(100, j, -1):
                str = graph[i][j:k]
                if str[0] != str[-1]:
                    continue
                reversed_str = str[::-1]
                if str == reversed_str:
                    ans = max(ans, len(str))

    reversed_graph = graph[::-1]
    round = list(zip(*reversed_graph))
    for i in range(100):
        for j in range(100):
            #가로
            for k in range(100, j, -1):
                str = round[i][j:k]
                if str[0] != str[-1]:
                    continue
                reversed_str = str[::-1]
                if str == reversed_str:
                    ans = max(ans, len(str))
    print('#{} {}'.format(t, ans))
