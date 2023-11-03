t = int(input())
dict = {}
r_dict = {}
i = j = 1
for n in range(1, 50000):
    dict[n] = (i, j); r_dict[(i,j)] = n
    i , j = i-1, j+1
    if i < 1:
        i, j = j, 1

for tc in range(1, t+1):

    p, q = map(int, input().split())
    pi, pj = dict[p]
    qi, qj = dict[q]
    ans = r_dict[(pi + qi, pj + qj)]
    print('#{} {}'.format(tc, ans));

