class Solution:
    def maxConsecutiveAnswers(self, a: str, k: int) -> int:
        left = 0
        temp = k
        for right in range(len(a)):
            if a[right] == 'F':
                temp -= 1
            if temp < 0:
                if a[left] == 'F':
                    temp += 1
                left += 1
        old = right - left + 1
        left = 0
        for right in range(len(a)):
            if a[right] == 'T':
                k -= 1
            if k < 0:
                if a[left] == 'T':
                    k += 1
                left += 1
        new = right - left + 1

        return max(old, new)