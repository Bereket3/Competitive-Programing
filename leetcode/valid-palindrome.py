class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ''
        for char in s:
            if char.isalnum():
                news += char.lower()
        left, right = 0, len(news)-1
        while left < right:
            if news[left] != news[right]:
                return False
            left += 1
            right -= 1
        return True
        