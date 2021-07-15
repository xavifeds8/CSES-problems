"""
LOVE
MOVIE
"""
str1 = input()
str2 = input()

dp = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]

for i in range(len(str1)+1):
    for j in range(len(str2)+1):
        if i == 0:
            dp[0][j] = j
        elif j==0:
            dp[i][0] = i

        elif str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1+min(dp[i-1][j-1], dp[i][j-1] ,dp[i-1][j])
print(dp[len(str1)][len(str2)])
