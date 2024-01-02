class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        left = 0
        right = len(num) - 1
        temp = 0

        while left < right:
            temp = num[left] + num[right]
            if temp == target:
                return [left +1, right +1]
            elif temp > target:
                right -= 1
            else:
                left += 1