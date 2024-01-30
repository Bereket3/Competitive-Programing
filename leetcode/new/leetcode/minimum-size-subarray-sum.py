class Solution(object):
    def minSubArrayLen(self, target, nums):
        
        l = 0
        csum = 0
        rst = float('inf')

        for i in range(len(nums)):
            csum += nums[i]
            while csum >= target:
                if i - l + 1 < rst:
                    rst = i - l + 1
                csum -= nums[l]
                l += 1
        return rst if rst != inf else 0