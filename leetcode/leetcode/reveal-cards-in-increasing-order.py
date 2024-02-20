class Solution:
    def deckRevealedIncreasing(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        qu = deque()
        
        for i in nums:
            if qu:
                qu.appendleft(qu.pop())
            qu.appendleft(i)

        return list(qu)