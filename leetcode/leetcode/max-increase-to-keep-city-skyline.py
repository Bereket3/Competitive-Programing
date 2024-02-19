class Solution:
    def maxIncreaseKeepingSkyline(self, m: List[List[int]]) -> int:
        r = len(m)
        c = len(m[0])

        r_max = []
        c_max = []

        for i in m:
            r_max.append(max(i))
        
        for j in zip(*m):
            c_max.append(max(j))

        res = 0
        
        for i in range(r):
            for j in range(c):
                res += (min(r_max[i], c_max[j]) - m[i][j])
            
        return res