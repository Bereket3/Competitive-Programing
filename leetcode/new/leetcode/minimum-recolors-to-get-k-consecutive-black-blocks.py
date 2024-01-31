class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_change = float('inf')
        if len(blocks) == k:
            return blocks.count('W')
        for i in range(len(blocks) - k + 1):
            print(i)
            min_change = min(min_change, blocks[i:i+k].count('W'))
        return min_change