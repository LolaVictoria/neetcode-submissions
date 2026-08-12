class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1]
        left = 1
        #left sum
        for i in range(len(nums)):
            left *= nums[i]
            left_product.append(left)
            

        right_product = [1]
        right = 1
        #right sum
        for i in range(len(nums) -1, 0, -1):
            right *= nums[i]
            right_product.append(right)
        right_product.reverse()

        prod = []
        for i in range(len(nums)):
            prod.append(left_product[i] * right_product[i])
        return prod


