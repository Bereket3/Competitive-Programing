class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(0, nums.__len__(), 2):
            current = nums[i:i+2]
            out+=[current[1]]*current[0]

        return out