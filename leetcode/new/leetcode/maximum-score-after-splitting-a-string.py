class Solution:
    def maxScore(self, s: str) -> int:
        max_sum = 0
        # my_list = list(map(int, s.split()))
        total_ones = s.count('1')
        total_zeros = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                total_zeros += 1
            else:
                total_ones -= 1
            max_sum = max(max_sum, total_ones + total_zeros)

        return max_sum