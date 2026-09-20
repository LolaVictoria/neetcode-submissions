class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        if len(nums) == 1:
            return nums[0]


        def dp(i):
            if i in memo:
                return memo[i]
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0], nums[1])

            result = max(nums[i] + dp(i - 2), dp(i - 1))
            memo[i] = result
            
            return result
        return dp(len(nums) - 1)

        