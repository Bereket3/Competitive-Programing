class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        equal = []
        above = []
        below = []

        for i in nums:
            if i == pivot:
                equal.append(i)
            elif i > pivot:
                above.append(i)
            else:
                below.append(i)

        return below+equal+above