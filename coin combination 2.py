# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 23:56:45 2021

@author: xavifeds
"""
p , n = map(int,input().split())
lst = list(map(int , input().split()))
dp = [0 for i in range(n+1)]
dp[0] =1
for j in lst:
    for i in range(0 , n+1):
        if i>=j:
            dp[i] = dp[i-j] + dp[i]
print(dp[n])