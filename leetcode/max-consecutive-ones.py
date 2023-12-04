class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxv = 0
        b = 0
        for char in nums:
            if char == 1:
                b += 1
            else:
                if maxv < b:
                    maxv = b
                b = 0
        return maxv if b < maxv else b