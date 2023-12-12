class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        my_dict = {}
        for a, b in reversed(operations):
            my_dict[a] = my_dict.get(b, b)
        
        for i, v in enumerate(nums):
            if v in my_dict:
                nums[i] = my_dict[v]
    
        return nums