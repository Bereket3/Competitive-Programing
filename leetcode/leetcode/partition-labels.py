class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c:i for i, c in enumerate(s)}
        end = 0
        res = []
        left = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if end == i:
                res.append(i-left + 1)
                left = max(left, last[c] + 1)
        return res