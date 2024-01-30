class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        postfix_product = 1
        result = [1]*n

        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        for i in range(n-1,-1,-1):
            result[i] *= postfix_product
            postfix_product *= nums[i]

        return result