class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        my_s1 = Counter(s1)
        my_s2 = Counter(s2[:len(s1)])
        for i in range(len(s1), len(s2)):
            if my_s1 == my_s2:
                return True
            my_s2[s2[i - len(s1)]] -= 1
            if my_s2[s2[i - len(s1)]] == 0:
                del my_s2[s2[i - len(s1)]]
            my_s2[s2[i]] += 1

        if my_s1 == my_s2:
            return True

        return False