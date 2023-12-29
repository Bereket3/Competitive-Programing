class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[0]*101
        out_put=[]
        for num in nums:
            count[num]+=1 
        for num in nums:
            out_put.append(sum(count[:num]))
        return out_put