n = int(input())
flower = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    flower.append([a * 100 + b, c * 100 + d])

flower.sort(key=lambda x: (x[0], -x[1]))
start = 301  #3월 1일
end = 1201  #12월 1일
cnt = 0
maxVal = 0
idx = 0

while start < end:
    isSelected = False

    for i in range(idx, n):
        if flower[i][0] > start:  #공백 발생 가능성 줄임
            break
        if flower[i][1] > maxVal:
            isSelected = True
            idx += 1
            maxVal = flower[i][1]

    if isSelected:
        start = maxVal
        cnt += 1
    else:
        break
if maxVal < end: #12월 1일까지 개화하는 꽃이 없으므로
    print(0)
else:
    print(cnt)