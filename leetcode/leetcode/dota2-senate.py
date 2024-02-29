class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        des = deque()
        res = deque()

        n = len(senate)

        for j, i in enumerate(senate):
            if i == 'R':
                res.append(j)
            else:
                des.append(j)
            

        while res and des:
            d = des.popleft()
            r = res.popleft()

            if r < d:
                res.append(r + n)
            else:
                des.append(d + n)
        

        return 'Radiant' if res else 'Dire'
            