N = int(input())
voca = []
for i in range(N):
    arr = list(input().split())
    voca.append(arr)

keys = set()
for i in range(N):
    flag = False
    str = ""
    for j in range(len(voca[i])):
        if voca[i][j][0].lower() not in keys and not flag:
            keys.add(voca[i][j][0].lower())
            if j != 0:
                str += " "
            str += "["+voca[i][j][0]+"]"+voca[i][j][1:]
            flag = True
        else:
            if j != 0:
                str += " "
            str += voca[i][j]
    if flag:
        print(str)
        continue
    #단축키로 지정 안 된 것이 있다면 단축키로 지정
    flag = False
    str = ""
    for j in range(len(voca[i])):
        for l in range(len(voca[i][j])):
            if voca[i][j][l].lower() not in keys and not flag:
                keys.add(voca[i][j][l].lower())
                str += "["+voca[i][j][l]+"]"
                flag = True
            else:
                str += voca[i][j][l]
        str += " "
    if flag:
        print(str)
    else:
        print(*voca[i])