class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(set(cards)) == len(cards):
            return -1

        contaner = {}
        out = len(cards)
        
        for i in range(len(cards)):
            if cards[i] in contaner:
                out = min(out, i - contaner[cards[i]] + 1)
                contaner[cards[i]] = i
            else:
                contaner[cards[i]] = i

        return out