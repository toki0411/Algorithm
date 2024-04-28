n = int(input())
for t in range(n):
    voca, s = input().split()
    cnt = 0
    cnt = voca.count(s)
    new_voca = voca.replace(s, "")
    print(cnt + len(new_voca))