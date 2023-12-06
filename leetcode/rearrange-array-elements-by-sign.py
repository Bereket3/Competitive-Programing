class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postive = []
        negative = []
        out = []
        for i in nums:
            if i < 0:
                negative.append(i)
            else:
                postive.append(i)

        for i in range(postive.__len__()):
            out.append(postive[i]);out.append(negative[i])
            
        return out