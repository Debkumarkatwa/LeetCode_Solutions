class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        
        max_profit, buy_date = 0, prices[0]
        for i in range(1,len(prices)):
            if prices[i] < buy_date:
                buy_date = prices[i]
            else:
                profit = prices[i] - buy_date
                if profit > max_profit:
                    max_profit = profit
            
            if prices[i] < buy_date:
                buy_date = prices[i]
        
        return max_profit



a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))  # Output: 5
print(a.maxProfit([7,6,4,3,1]))  # Output: 0
print(a.maxProfit([2,1,4]))  # Output: 3