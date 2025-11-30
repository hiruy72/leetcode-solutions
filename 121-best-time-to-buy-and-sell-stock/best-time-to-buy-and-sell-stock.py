class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_num = float('inf')

        for price in prices:
            min_num = min(price, min_num)
            profit = price - min_num
            max_profit = max(profit , max_profit)
        return max_profit
            
            

            

            






       
