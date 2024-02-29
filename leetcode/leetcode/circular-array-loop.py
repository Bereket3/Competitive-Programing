class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        def find_n(index):
            return (index + nums[index])%len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
        
            s = i
            f = find_n(i)
            
            while nums[f] * nums[s] > 0 and nums[find_n(f)] * nums[s] > 0:
                if s == f:
                    if s != find_n(s):
                        return True
                    break

                s = find_n(s)
                f = find_n(find_n(f))
            index = i

            while nums[index] * nums[find_n(index)] > 0:
                next_index = find_n(index)
                nums[index] = 0
                index = next_index

        return False