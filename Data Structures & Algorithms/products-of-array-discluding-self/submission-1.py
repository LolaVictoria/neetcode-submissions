class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res

        #t. c - O(n)  s.c = O(n * m)
        # left_product = [1]
        # left = 1
        # #left sum
        # for i in range(len(nums)):
        #     left *= nums[i]
        #     left_product.append(left)
            

        # right_product = [1]
        # right = 1
        # #right sum
        # for i in range(len(nums) -1, 0, -1):
        #     right *= nums[i]
        #     right_product.append(right)
        # right_product.reverse()

        # prod = []
        # for i in range(len(nums)):
        #     prod.append(left_product[i] * right_product[i])
        # return prod


