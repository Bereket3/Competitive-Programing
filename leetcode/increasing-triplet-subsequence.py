class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = float("inf")
        mid = float("inf")

        for i in nums:
            if i <= small:
                small = i
            elif i <= mid:
                mid = i
            else:
                return True
        
        return False