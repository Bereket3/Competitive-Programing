class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        curr_sum = sum(nums[:3])
        nums.sort()
        out = curr_sum
        for i in range(nums.__len__() - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(curr_sum - target) < abs(out - target):
                    out = curr_sum
                if curr_sum == target:
                    return target
                if curr_sum > target:
                    right -= 1
                else:
                    left += 1

        return out