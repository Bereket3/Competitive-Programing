class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        c.sort()
        out = []

        def help(start, curr_sum, path):
            if curr_sum == target:
                out.append(path[:])
                return 
            
            if curr_sum > target:
                return 
            
            for i in range(start, len(c)):
                if i > start and c[i] == c[i - 1]:
                    continue
                
                path.append(c[i])
                help(i + 1, curr_sum + c[i], path)
                path.pop()

        help(0,0,[])
        return out