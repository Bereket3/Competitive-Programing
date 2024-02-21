class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        tot = nums[0]
        max_ = nums[0]
        
        if max_ == max(nums):
            return max_

        for i in range(1, len(nums)):
            tot += nums[i]
            max_ = max(max_, math.ceil(tot  / (i + 1)))
        return max_