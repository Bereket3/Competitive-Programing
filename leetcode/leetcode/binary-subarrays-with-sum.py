class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        return no of non-empty subarrays with sum goal
        """
        mapper = Counter()
        mapper[0] = 1
        out = pri = 0
        for i in nums:
            pri += i
            out += mapper.get(pri - goal, 0)
            mapper[pri] += 1

        return out
