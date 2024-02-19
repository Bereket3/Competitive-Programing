class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        left = out = 0
        running_sum = 1
       
        while running_sum <= n:
            if left < len(nums) and running_sum >= nums[left]:
                running_sum += nums[left]
                left += 1
            else:
                out += 1
                running_sum *= 2
        return out