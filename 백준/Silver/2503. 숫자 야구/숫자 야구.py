n = int(input())
cmd = []
for _ in range(n):
    num, strike, ball = map(int, input().split())
    cmd.append([num, strike, ball])
ans =0
for i in range(1, 10):
    for j in range(1, 10):
        for l in range(1, 10):
            if i == j or j == l or l == i :
                continue
            number = 100*i + 10*j + l
            # print(number)
            cnt = 0
            for cm in cmd:
                num, strike, ball = cm[0], cm[1], cm[2]
                s_cnt = 0; b_cnt = 0
                tmp_num = num;
                a = tmp_num // 100
                b = (tmp_num % 100) // 10
                c = ((tmp_num % 100) % 10)
                tmp_list = [a,b,c]
                if a == i:
                    s_cnt += 1
                elif i in tmp_list:
                    b_cnt += 1

                if b == j:
                    s_cnt += 1
                elif j in tmp_list:
                    b_cnt += 1

                if c == l:
                    s_cnt += 1
                elif l in tmp_list:
                    b_cnt += 1

                if b_cnt == ball and s_cnt == strike:
                    cnt += 1
            if cnt == n:
                ans += 1

print(ans)