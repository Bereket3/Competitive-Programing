class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pri = [0]*len(nums)
        for i, j in requests:
            pri[i] += 1
            if j < len(nums) - 1:
                pri[j + 1] -= 1
            

        for i in range(1, len(nums)):
            pri[i] += pri[i - 1]

        pri.sort()
        nums.sort()
        my_sum = 0
       

        for i in range(len(nums) - 1, -1, -1):
            my_sum += (pri[i]*nums[i])
           

        return int(my_sum %( 10**9+7))
