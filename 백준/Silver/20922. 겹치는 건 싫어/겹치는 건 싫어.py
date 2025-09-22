N, K = map(int, input().split())

num = list(map(int, input().split()))
left = 0
ans = 0
cnt = [0] * 100001
for right in range(N):
    cnt[num[right]] += 1
    # K 초과 → 왼쪽 포인터 이동시키며 개수 줄임
    while cnt[num[right]] > K:
        cnt[num[left]] -= 1
        left += 1

    ans = max(ans, right - left + 1)

print(ans)