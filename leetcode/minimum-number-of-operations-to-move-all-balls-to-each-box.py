class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0]*len(boxes)
        for i in range(boxes.__len__()):
            for j in range(len(boxes)):
                if boxes[j] != '0' and i != j:
                    answer[i] += abs(i-j)


        return answer