class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def help(index):
            if index == n:
                out.append(c[:])
            
            for i in range(len(nums)):
                if not v[i]:
                    v[i] = True
                    c[index] = nums[i]
                    help(index + 1)
                    v[i] = False


        n = len(nums)
        v = [False] * n
        c = [0] * n
        out = []
        help(0)
        return out 
