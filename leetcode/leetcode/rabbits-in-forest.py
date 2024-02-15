class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = 0
        mp = {}
        for an in answers:
            if an == 0:
                count += 1
            elif an not in mp or mp[an] == 0:
                mp[an] = 1
                count += an + 1
            else:
                mp[an] += 1
                if mp[an] > an:
                    mp[an] = 0
        return count