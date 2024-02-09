class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i, j in enumerate(nums):
            if j % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        left = out = one_count = count = 0

        for right in range(len(nums)):

            if nums[right] == 1:
                one_count += 1
                count = 0
            
            if one_count == k:
                
                while left < len(nums) and nums[left] == 0:
                    count += 1
                    left += 1
                one_count -= 1
                count += 1
                left += 1
            out += count

        return out