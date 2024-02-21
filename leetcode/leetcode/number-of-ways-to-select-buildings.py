class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        one = zero = one_zero = zero_one = 0
        ans = 0
        for c in s:
            if c == '0':
                zero += 1
                one_zero += one
                ans += zero_one
            else:
                one += 1
                zero_one += zero
                ans += one_zero
        return ans