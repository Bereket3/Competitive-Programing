class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pri = nums[0]
        out = []
        for i in range(1, nums.__len__()):
            out.append(pri)
            pri += nums[i]
        out.append(pri)

        return out
