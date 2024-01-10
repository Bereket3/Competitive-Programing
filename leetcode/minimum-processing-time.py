class Solution:
    def minProcessingTime(self, p: List[int], t: List[int]) -> int:
        p.sort()
        t.sort(reverse = True)
        max_out = 0
        for i, j in enumerate(p):
            max_out = max(max_out, max([k + j for k in t[i*4:i*4 + 4]]))
        return max_out