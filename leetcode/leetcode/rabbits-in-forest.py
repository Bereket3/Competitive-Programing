class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = 1
        answers.sort()
        tot = answers[0] + 1

        for i in range(1, len(answers)):
            if answers[i] != answers[i-1] or answers[i] - count + 1 == 0:
                count = 1
                tot += answers[i] + 1
            else:
                count += 1

        return tot