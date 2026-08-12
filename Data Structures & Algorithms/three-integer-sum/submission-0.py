class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for curr in range(len(nums)):
            if curr > 0 and nums[curr] == nums[curr - 1]:
                continue
            left = curr + 1
            right = len(nums) - 1

            while left < right:
                num_sum = nums[curr] + nums[left] + nums[right]

                if num_sum > 0:
                    right -= 1
                elif num_sum < 0:
                    left += 1
                else:
                    res.append([nums[curr], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1

        return res
            
        