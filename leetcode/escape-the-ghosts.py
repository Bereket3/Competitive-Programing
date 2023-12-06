class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_step = abs(0 - target[0]) + abs(0 - target[1])
        for i in ghosts:
            temp = abs(i[0] - target[0]) + abs(i[1] - target[1])
            if temp <= my_step:
                return False
        return True
