class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        out = []

        def help(i, p):
            if len(p) == k:
                out.append(p[:])
                return 
            if i >= n: return

            p.append(nums[i])
            help(i + 1, p)
            p.pop()

            help(i + 1, p)
        
        help(0, [])
        return out