class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cont = 0
        for i in range(nums.__len__()):
            for j in range(i):
                if nums[i] == nums[j]:
                    cont += 1
        return cont


        