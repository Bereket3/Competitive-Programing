class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        """
        the number of distinct element in array == the number of distinct elemnt 
        in the suub array
        """
        total = Counter(nums)
        k = total.__len__()
        count = 0
        window = Counter()

        for right in range(len(nums)):
            window = Counter()
            for j in range(right, len(nums)):
                window[nums[j]] += 1
                if len(window) == k:
                    count += 1
            
                
        return count