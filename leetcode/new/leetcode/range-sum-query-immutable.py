class NumArray:
    def __init__(self, nums: List[int]):
        self.numbers = [0]
        for i in range(len(nums)):
            self.numbers.append(nums[i]+self.numbers[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.numbers[right+1]-self.numbers[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)