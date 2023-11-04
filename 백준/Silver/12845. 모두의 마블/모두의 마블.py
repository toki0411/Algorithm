n = int(input())
card = list(map(int, input().split()))
card.sort(reverse=True)
higest_card = card[0]
ans = 0
for i in range(1, len(card)):
    ans += higest_card + card[i]
print(ans)