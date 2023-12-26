class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        one = one_2 = Counter(nums)[1]
        zeros = zeros_2 = high = 0
        out = []

        for j in nums:
            high = max(high, one+zeros)
            if j == 1:
                one -= 1
            else:
                zeros += 1

        high = max(high, one+zeros)

        for i, j in enumerate(nums):
            if high == one_2 + zeros_2:
                out.append(i)
            if j == 1:
                one_2 -= 1
            else:
                zeros_2 += 1

        if high == one_2 + zeros_2:
            out.append(len(nums))
        
        return out