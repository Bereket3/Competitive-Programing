class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = []
        first = nums[:n]
        second = nums[n:]
        for i in range(len(first)):
            out.append(first[i])
            out.append(second[i])
        return out