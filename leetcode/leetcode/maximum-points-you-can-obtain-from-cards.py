class Solution:
    def maxScore(self, c: List[int], k: int) -> int:
        total = sum(c)
        n = len(c)
        notto = n - k
        window_sum = sum(c[:notto])
        min_sum = window_sum

        for i in range(notto, n):
            window_sum = window_sum - c[i - notto] + c[i]
            min_sum = min(min_sum, window_sum)

        return total - min_sum