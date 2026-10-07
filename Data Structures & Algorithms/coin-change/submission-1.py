class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amt):
            if amt == 0:
                return 0
            if amt < 0:
                return float('inf')
            if amt in memo:
                return memo[amt]

            best = float('inf')
            for coin in coins:
                remainder = amt - coin
                curr = dfs(remainder)
                best = min(best, curr + 1)
            memo[amt] = best
            return best
        result = dfs(amount)
        return result if result != float('inf') else -1

        
        


        # dp = [float('inf')] * (amount + 1)
        # dp[0] = 0

        # for a in range(1, amount + 1):
        #     for coin in coins:
        #         remainder = a - coin
        #         if remainder >= 0:
        #             dp[a] = min(dp[a], 1 + dp[remainder])
        # return dp[amount] if dp[amount] !=float('inf') else -1
