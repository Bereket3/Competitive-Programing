class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if s.__len__() < p.__len__():return []

        scout = Counter(s[:p.__len__()])
        window = Counter(p)
        contain = []
        l = 0

        for i, j in enumerate(s[p.__len__():]):
            if window == scout:
                contain.append(l)

            scout[s[l]] -= 1

            if scout[s[l]] == 0:
                del scout[s[l]]

            l += 1
            scout[j] += 1

        if window == scout:
            contain.append(l)
        
        return contain
