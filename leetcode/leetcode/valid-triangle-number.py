class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0

        k = len(nums) - 1
        out = 0
        nums.sort()

        while k >= 2:
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    out += j - i
                    j -= 1
                else:
                    i += 1
            k -= 1

        return out
        
        