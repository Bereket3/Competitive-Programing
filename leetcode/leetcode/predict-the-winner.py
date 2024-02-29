class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        #keep only the difference
        def score(i,j):
            return (i<=j) and max(nums[i]-score(i+1,j),nums[j]-score(i,j-1))
        return score(0,len(nums)-1)>=0
