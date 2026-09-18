class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max, curr_min = nums[0], nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            candidates = (curr_max * nums[i], curr_min * nums[i], nums[i])

            curr_max = max(candidates)
            curr_min = min(candidates)
            result = max(result, curr_max)
        return result



        