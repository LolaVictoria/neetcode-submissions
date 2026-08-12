class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_sum = {}

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in hash_sum:
                return [hash_sum[rem], i]
            hash_sum[nums[i]] = i
        