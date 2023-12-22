class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]

        for i, val in enumerate(image):
            for j in range(len(val)):
                if val[j] == 0:
                    val[j] = 1
                else:
                    val[j] = 0

        return image