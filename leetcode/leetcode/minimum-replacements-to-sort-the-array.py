class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        last = nums[-1]
        for i in range(len(nums) -1, -1, -1):
            if last >= nums[i]:
                last = nums[i]
                continue
            if nums[i] % last == 0:
                temp = nums[i]//last
            else:
                temp = nums[i]//last + 1
                last = nums[i]//temp
            res += temp - 1
        return res