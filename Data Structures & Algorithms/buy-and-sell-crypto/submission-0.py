class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        slow = 0

        for fast in range(len(prices)):
            while prices[slow] > prices[fast]:
                slow += 1
            profit = prices[fast] - prices[slow]
            max_profit = max(max_profit, profit)
        return max_profit

        