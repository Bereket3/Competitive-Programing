class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_reminder = sum(nums) % p

        if total_reminder == 0:
            return 0

        mapper = Counter()
        mapper[0] = -1

        n = len(nums)
        cur = 0
        res = n

        for i, num in enumerate(nums):
            cur = (cur + num) % p
            if mapper.get((cur-total_reminder)%p) is not None:
                res = min(res, i - mapper.get((cur-total_reminder)%p))
            mapper[cur] = i

        if res >= n:
            return -1

        return res