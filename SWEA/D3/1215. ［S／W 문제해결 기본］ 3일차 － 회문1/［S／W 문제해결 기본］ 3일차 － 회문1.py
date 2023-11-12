for tc in range(1,11):
    l = int(input())
    ans = 0
    graph = [list(input()) for _ in range(8)]
    for i in range(8):
        for j in range(8-l+1):
            str = graph[i][j:j+l]
            key = True
            if len(str) == 1: ans += 1 ;break

            for k in range(len(str)//2 ):
                if str[k] != str[len(str)-k-1]:
                    key = False
                    break
            if key :
                ans +=1

        for j in range(8-l+1):
            str = []
            for k in range(j, j+l):
                str.append(graph[k][i])

            key = True
            if len(str) == 1: ans += 1 ;break

            for k in range(len(str)//2 ):
                if str[k] != str[len(str)-k-1]:
                    key = False
                    break
            if key :
                ans +=1

    print('#{} {}'.format(tc, ans))

