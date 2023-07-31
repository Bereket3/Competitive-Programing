class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        out_put = []
        for i in range(len(nums)):
            if nums[i] == target:
                out_put.append(i)
        return out_put
