class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        contaner = defaultdict(list)
        out = [0]*len(nums)

        for indx, val in enumerate(nums):
            contaner[val].append(indx)
       
        def solver(x):
            arr = contaner[x]

            total = 0
            for i in range(1, len(arr)):
                total += arr[i] - arr[0]

            out[arr[0]] = total

            for i in range(1, len(arr)):
                total += (arr[i] - arr[i-1])*(i)
                total -= (arr[i] - arr[i-1])*(len(arr) - (i))
                out[arr[i]] = total

        for i in contaner.keys():
            if contaner[i].__len__() > 1:
                solver(i)
            else:
                out[contaner[i][0]] = 0

        return out
                
