dx = [0,-1,0,1,0]
dy = [0,0,1,0,-1]
T = int(input())
for tc in range(1, T+1):
    graph = [[0] * 11 for _ in range(11)]
    total = 0
    time, num = map(int, input().split()) #총 시간, 충전소 개수
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.append(0); B.append(0)
    charge = []
    for i in range(num):
        x, y, c, p = map(int, input().split()) # 좌표, 충전범위, 성능
        charge.append([y,x,c,p])

    ax = 1; ay = 1 #초기위치 설정
    bx = 10; by = 10
    for t in range(len(A)):
        #print(ax, ay)
        ac = []; bc = []
        #A가 현재위치에서 충전할 수 있는 충전소 찾음
        for i in range(num):
            if abs(charge[i][0] - ax) + abs(charge[i][1] - ay) <= charge[i][2]:
                ac.append(i)
            if abs(charge[i][0] - bx) + abs(charge[i][1] - by) <= charge[i][2]:
                bc.append(i)
        max_charge = 0
        if len(ac) > 0 and len(bc) > 0 :
            for i in range(len(ac)):
                for j in range(len(bc)):
                    if ac[i] == bc[j]:
                        val = charge[ac[i]][3] // 2
                        val += charge[bc[j]][3] // 2
                        max_charge = max(val, max_charge)
                    else:
                        val = charge[ac[i]][3] + charge[bc[j]][3]
                        max_charge = max(val, max_charge)
            total += max_charge
        elif len(ac) > 0 and len(bc) == 0:
            for i in range(len(ac)):
                val = charge[ac[i]][3]
                max_charge = max(val, max_charge)
            total += max_charge
        elif len(bc) > 0 and len(ac) == 0:
            for i in range(len(bc)):
                val = charge[bc[i]][3]
                max_charge = max(val, max_charge)
            total += max_charge
        dirA = A[t];
        dirB = B[t]
        ax += dx[dirA];
        bx += dx[dirB]
        ay += dy[dirA];
        by += dy[dirB]
        # print(t, max_charge)
    print("#{} {}".format(tc, total))