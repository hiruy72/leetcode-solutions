from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k]: max coins at (i,j) using k neutralizations
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # start position
        for k in range(3):
            if coins[0][0] < 0 and k > 0:
                dp[0][0][k] = 0  # neutralize
            else:
                dp[0][0][k] = coins[0][0]
        
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if i == 0 and j == 0:
                        continue
                    
                    val = coins[i][j]
                    
                    # from top
                    if i > 0:
                        # no neutralization
                        dp[i][j][k] = max(
                            dp[i][j][k],
                            dp[i-1][j][k] + val
                        )
                        
                        # use neutralization
                        if val < 0 and k > 0:
                            dp[i][j][k] = max(
                                dp[i][j][k],
                                dp[i-1][j][k-1]
                            )
                    
                    # from left
                    if j > 0:
                        # no neutralization
                        dp[i][j][k] = max(
                            dp[i][j][k],
                            dp[i][j-1][k] + val
                        )
                        
                        # use neutralization
                        if val < 0 and k > 0:
                            dp[i][j][k] = max(
                                dp[i][j][k],
                                dp[i][j-1][k-1]
                            )
        
        return max(dp[m-1][n-1])