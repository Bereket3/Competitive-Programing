class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        all_set= set(fronts + backs)

        for f,b in zip(fronts, backs):
            if f == b:
                all_set.discard(f)
        
        return min(all_set, default = 0)