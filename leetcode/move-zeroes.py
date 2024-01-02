class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        try:
            left = nums.index(0)
            right = left + 1
            

            while right < len(nums):
                if nums[right] == 0:
                    right += 1
                elif nums[right] != 0:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right += 1
        except:...