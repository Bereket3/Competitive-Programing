class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # sort the list
        nums.sort(reverse = True)
        # find the smallest number
        smallest = nums[-1]
        
        # count the friquency of the number
        unique = Counter(nums)
        the_list = list(unique.keys())

        # initalize the container for counting operations
        count = 0
        next_count = 0
        for index, i in enumerate(the_list):
            if i != smallest:
                one_step = unique[i] + next_count
                count += one_step
                next_count = one_step
        return count