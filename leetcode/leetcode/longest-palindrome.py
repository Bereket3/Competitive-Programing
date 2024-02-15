class Solution:
    def longestPalindrome(self, s: str) -> int:
        my_count = Counter(s)
        if len(my_count) == 1:
            return my_count[s[0]]
        evens = 0
        for i in my_count:
            if my_count[i]% 2 == 0:
                evens += my_count[i]
        odds = 0
        one = False
        for i in my_count:
            if my_count[i] % 2 != 0:
                if not one:
                    odds += my_count[i]
                    one = True
                    continue
                odds += my_count[i] - 1

        res = evens + odds

        return res if res != 0 else 1