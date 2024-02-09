class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        out = [0]*len(nums)
        pri = sum(nums)
        suffix = 0
        for i in range(nums.__len__()):
            pri -= nums[i]
            out[i] = (nums[i]*i - suffix + pri - nums[i]*(len(nums) - i - 1))
            suffix += nums[i]
            
        return out