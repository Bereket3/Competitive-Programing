class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr_wind = max_window = 0
        n = len(nums)
        for right in range(n):
            if nums[right] == 1:
                curr_wind += 1
            elif nums[right] == 0:
                if right + 1 < n and nums[right + 1] == 1:
                    left = right + 1
                    while left < n and nums[left] != 0:
                        curr_wind += 1
                        left += 1
                max_window = max(curr_wind, max_window)
                curr_wind = 0

        max_window = max(max_window, curr_wind)
        return max_window if max_window != n else n - 1