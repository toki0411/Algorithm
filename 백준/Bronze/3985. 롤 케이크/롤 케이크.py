cakelength = int(input())
people = int(input())
cake = [0] * 1000
max_expected = -1; max_get = -1; expected_ans = 0
for i in range(1, people+1):
    start, end = map(int, input().split())
    if (end - start) > max_expected:
        expected_ans = i
        max_expected = (end - start)
    for j in range(start, end+1):
        if not cake[j]:
            cake[j] = i
ans = 0
for c in range(1, people+1):
    val = cake.count(c)
    if val > max_get:
        ans = c
        max_get = val

print(expected_ans)
print(ans)
