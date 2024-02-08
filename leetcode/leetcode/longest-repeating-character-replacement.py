class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        my_contaner = Counter()
        left = min_length = out = 0
        
        for right in range(len(s)):
            my_contaner[s[right]] += 1
            min_length = max(min_length, my_contaner[s[right]])
            
            if right - left + 1 - min_length > k:
                my_contaner[s[left]] -= 1
                left += 1
            else:
                out = max(out, right - left + 1)

        return out