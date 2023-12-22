class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        flag = arr[0] < arr[1]
        if not flag: return False
        count = 0

        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                return False
            else:
                if flag:
                    if arr[i-1] > arr[i]:
                        flag = False
                        count += 1  
                elif not flag:
                    if arr[i-1] < arr[i]:
                        count += 1
                        flag = True

        return True if count == 1 else False