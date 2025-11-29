class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_num = float("inf") 

        for price in prices:
            if price < min_num:
                min_num = price
            profit = price - min_num
            max_profit= max(profit, max_profit)
        return max_profit
            






       
