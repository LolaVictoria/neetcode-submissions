class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            memo = {}
            def dp(i):

                if i in memo:
                    return memo[i]
                if i == 0:
                    return houses[i]
                if i == 1:
                    return max(houses[0], houses[1])

                result = max(dp(i - 2) + houses[i], dp(i - 1))        
                memo[i] = result
                return result
            return dp(len(houses) - 1)
        return max(rob_line(nums[1:]), rob_line(nums[:-1]))