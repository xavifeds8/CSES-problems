# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 23:32:10 2021

@author: xavifeds
"""
n = int(input())
dp = [10000000]*(n+1)
dp[0] = 0
dp
for i in range(1 , n+1 ):
    res = str(i)
    for j in res:
        if int(j)>i:continue
        dp[i] = min(dp[i] , dp[i-int(j)]+1)
print(dp[n])