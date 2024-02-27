class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def help(index, c):
            if index == len(nums):
                out.append(c[:])
                return 

            help(index + 1, c)
            c.append(nums[index])
            help(index + 1, c)
            c.pop()

        out = []
        help(0, [])
        return out