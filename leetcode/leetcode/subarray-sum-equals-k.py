class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [-1,-1,0] 0
        hmap = {0 : 1}
        res = 0
        total = 0
        
        for i in nums:
            total += i
            res += hmap.get(total - k, 0)
            hmap[total] = 1 + hmap.get(total, 0)
            
        return res