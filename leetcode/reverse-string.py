class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(s.__len__()//2):
            s[i], s[len(s) - i -1] = s[len(s)-i-1], s[i]