class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_now = nums[0]
        st = []
        for i in nums[1:]:
            while st and st[-1][0] <= i:
                st.pop()
            if st and i > st[-1][1]:
                return True

            st.append([i, min_now])
            min_now = min(min_now, i)

        return False
