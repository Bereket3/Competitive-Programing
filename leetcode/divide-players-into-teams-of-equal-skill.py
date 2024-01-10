class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        first_half = skill[:len(skill) // 2]
        second_half = skill[len(skill) // 2:][::-1]
        out = 0
        check = first_half[0] + second_half[0]
        for i, j in zip(first_half, second_half):
            if check != i + j:
                return -1
            out += i*j
        return out