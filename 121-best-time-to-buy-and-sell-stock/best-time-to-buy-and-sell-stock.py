class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_num = float('inf') # it will take the largest number

        for price in prices:
            if price < min_num:
                min_num = price
            profit = price - min_num
            if profit > max_profit:
                max_profit = profit
        return max_profit



       
