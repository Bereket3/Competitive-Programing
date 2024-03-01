class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        out = []
        def help(st, _sum, path):
            if _sum == 0 and len(path) == k:
                out.append(path[:])
            
            if st > 9:
                return 

            if _sum < st or len(path) >= k:
                return 
            
            
            path.append(st)
            help(st + 1, _sum - st, path)
            path.pop()
            help(st + 1, _sum, path)
        
        help(1, n, [])
        return out