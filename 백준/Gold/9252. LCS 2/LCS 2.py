s1 = [""]+list(input())
s2 = [""]+list(input())
dp = [['' for _ in range(len(s2))] for _ in range(len(s1))]
for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + s1[i]

        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
# print(dp)
if len(dp[-1][-1]) == 0:
    print(0)
else:
    print(len(dp[-1][-1]))
    print(dp[-1][-1])