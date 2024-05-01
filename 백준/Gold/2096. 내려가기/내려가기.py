import copy
n = int(input())
minDp = [0,0,0]
maxDp = [0,0,0]
for i in range(n):
    a,b,c = map(int, input().split())
    minDp = [min(minDp[0], minDp[1]) + a, min(minDp[0], minDp[1], minDp[2]) + b, min(minDp[2], minDp[1]) + c]
    maxDp = [max(maxDp[0], maxDp[1]) + a , max(maxDp[0], maxDp[1], maxDp[2]) + b,max(maxDp[2], maxDp[1]) + c]

print(max(maxDp), min(minDp))