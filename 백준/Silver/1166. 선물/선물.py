N, L, W, H = map(int, input().split())  #박스가 N개
ans = 0
start = 0
end = max(L, W, H)
for i in range(100):
    mid = (start + end) / 2
    if (L // mid) * (W // mid) * (H // mid) >= N:
        ans = max(mid, ans)
        start = mid
    else:
        end = mid
print(ans)