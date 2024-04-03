def rotateClock(idx):
    magnetic[idx].insert(0, magnetic[idx][-1])
    magnetic[idx].pop()


def rotateReverse(idx):
    magnetic[idx].append(magnetic[idx][0])
    magnetic[idx].remove(magnetic[idx][-1])


T = int(input())
for tc in range(1, T + 1):
    score = 0
    K = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(4)]
    cmd = [list(map(int, input().split())) for _ in range(K)]
    for c in cmd:
        idx, direction = c[0] - 1, c[1]
        leftList = []
        rightList = []
        for left in range(idx -1, -1, -1):
            leftIdxMagnetic = magnetic[left + 1][6]
            leftMagnetic = magnetic[left][2]
            leftList.append([left, leftMagnetic, leftIdxMagnetic])

        for right in range(idx +1, 4):
            rightIdxMagnetic = magnetic[right - 1][2]
            rightMagnetic = magnetic[right][6]

            rightList.append([right, rightMagnetic, rightIdxMagnetic])
        # print(leftList, "|",rightList)
        if direction == 1:  # 시계 방향
            rotateClock(idx)
        else:  # 반시계 방향
            rotateReverse(idx)


        if direction == 1:
            leftDir = -1
            rightDir = -1
        else:
            leftDir = 1
            rightDir = 1
        # idx의 왼쪽 자석을 돌린다.

        for i in range(len(leftList)):
            left, leftMagnetic, leftIdxMagnetic = leftList[i]
            if leftMagnetic != leftIdxMagnetic:
                if leftDir == 1:
                    rotateClock(left)
                    leftDir = -1
                else:
                    rotateReverse(left)
                    leftDir = 1
            else:
                break


        # idx의 오른쪽 자석을 돌린다.
        for i in range(len(rightList)):
            right, rightMagnetic, rightIdxMagnetic = rightList[i]
            if rightMagnetic != rightIdxMagnetic:
                if rightDir == 1:
                    rotateClock(right)
                    rightDir = -1
                else:
                    rotateReverse(right)
                    rightDir = 1
            else:
                break
        # print(magnetic)
    sScore = 1
    # 점수를 계산한다
    # print(magnetic)
    for i in range(4):
        if magnetic[i][0]:
            score += sScore
        sScore *= 2

    print("#{} {}".format(tc, score))
