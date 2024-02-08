class Solution:
    def balancedString(self, s: str) -> int:
        out = len(s)
        total_count = Counter(s)
        apperance = len(s) // 4
        
        extras = {}

        for key in total_count:
            if total_count[key] > apperance:
                extras[key] = total_count[key] - apperance
            
        if not extras: return 0

        left = 0
        for right in range(len(s)):
            if s[right] in extras:
                extras[s[right]] -= 1
            
            while max(extras.values()) <= 0:
                out = min(right - left + 1, out)

                if s[left] in extras:
                    extras[s[left]] += 1
                left += 1

        return out