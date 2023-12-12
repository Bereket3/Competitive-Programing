class Solution:
    def reverseWords(self, s: str) -> str:
        my_splited = s.split()
        return ' '.join(my_splited[::-1])