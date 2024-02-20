class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        s = [len(nums) - 1]
        ans = [0]*len(nums)

        for i in range(len(nums) - 2, -1, -1):
            while s and nums[i] >= nums[s[-1]]:
                s.pop()
            if s:
                ans[i] = s[-1] - i
            s.append(i)

        return ans