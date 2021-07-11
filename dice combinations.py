# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 22:27:52 2021

@author: xavifeds
"""
mod = 1000000007
n = int(input())
dp = [0]*(n+1)
dp[0], dp[1] = 1 , 1
for i in range(2,n+1):
    for j in range(1,7):
        if j>i: break
        dp[i]  = (dp[i]%mod  + dp[i-j]%mod)%mod
print(dp[n]%mod)