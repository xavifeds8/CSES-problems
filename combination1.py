# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 00:40:12 2021

@author: xavifeds
"""

n , val = map(int , input().split())

lst = list(map(int , input().split()))

dp = [0]*(val+1)

dp[0] = 1

for i in range(1 , val+1):
    for j in lst:
        if i>=j:
            dp[i]  += dp[i-j]
print(dp[val])