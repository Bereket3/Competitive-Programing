class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        return no of non-empty subarrays with sum goal
        """
        mapper ={0:1}
        out = pri = 0
        for i in nums:
            pri += i
            out += mapper.get(pri - goal, 0)
            mapper[pri] = mapper.get(pri, 0) + 1

        return out
