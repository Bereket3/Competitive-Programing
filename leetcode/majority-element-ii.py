class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        the_all = Counter(nums)
        out = []
        apperance = nums.__len__()//3 + 1
        for i in the_all:
            if the_all[i] >= apperance:
                out.append(i)
        return out