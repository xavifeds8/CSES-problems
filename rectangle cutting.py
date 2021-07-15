a , b = map(int , input().split())

dp = [[10**9 for i in range(b+1)] for j in range(a+1)]

for i in range(a+1):
    for j in range(b+1):
        if i==j:
            dp[i][j] = 0
            continue
        #vertical cuts
        for k in range(1 ,  i):
            dp[i][j] = min(dp[i][j]  , 1+dp[k][j]+dp[i-k][j])
        for k in range(1 , j):
            dp[i][j]  = min(dp[i][j] , 1+ dp[i][k]+dp[i][j-k])
print(dp[-1][-1])