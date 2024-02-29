class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        se = set()
        def help(index, c):
            if index == len(nums):
                if tuple(sorted(c)) not in se:
                    se.add(tuple(sorted(c)))
                    out.append(c[:])
                return 

            help(index + 1, c)
            c.append(nums[index])
            help(index + 1, c)
            c.pop()

        out = []
        help(0, [])
        return out