p = int(input())
for pc in range(1,p+1):
    height = list(map(int,input().split()))
    height = height[1:]
    ans = 0
    for i in range(1, len(height)):
        idx = 0; key = False
        for j in range(i-1, -1, -1):
            if height[j] > height[i]:
                key = True
                idx = j
        tmp = height[i]

        if key:
            for j in range(i - 1, idx-1, -1):
                height[j+1] = height[j]
                ans += 1
            height[idx] = tmp

    print(pc, ans)
