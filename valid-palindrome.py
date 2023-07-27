import re
class Solution(object):
    def isPalindrome(self, s):
        s=re.sub(r'[\W_]', '',s).lower()
        return s == s[::-1]
