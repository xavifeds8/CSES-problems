n,x = map(int , input().split())
price = list(map(int , input().split()))
pages = list(map(int , input().split()))
price.insert(0 , 0)
pages.insert(0,0)

dp = [[0 for i in range(x +1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,x+1):
        if price[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j]  , dp[i-1][j-price[i]]+pages[i])
print(dp[-1][-1])
        