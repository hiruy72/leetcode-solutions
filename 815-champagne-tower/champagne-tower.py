class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Create triangle with zeros
        dp = [[0] * (r + 1) for r in range(query_row + 1)]
        
        # Pour all into top
        dp[0][0] = poured
        
        # Fill row by row
        for r in range(query_row):
            for c in range(len(dp[r])):
                if dp[r][c] > 1:
                    overflow = (dp[r][c] - 1) / 2
                    dp[r + 1][c] += overflow
                    dp[r + 1][c + 1] += overflow
        
        return min(1, dp[query_row][query_glass])
