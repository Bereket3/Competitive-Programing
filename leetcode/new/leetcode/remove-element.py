class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n, i, got = len(nums) - 1, len(nums) - 1, 0
        while i >= 0:
            if nums[i] == val:
                nums[i] = nums[n-got]
                got += 1
            i -= 1
        return len(nums) - got
        