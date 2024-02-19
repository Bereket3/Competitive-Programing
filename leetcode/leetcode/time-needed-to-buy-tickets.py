class Solution:
    def timeRequiredToBuy(self, nums: List[int], k: int) -> int:
        score = 0
        it_k = nums[k]


        for i in range(it_k):
            for j in range(len(nums)):
                if nums[k] == 0:
                    break
                if nums[j] > 0:
                    nums[j] -= 1
                    score += 1
        return score