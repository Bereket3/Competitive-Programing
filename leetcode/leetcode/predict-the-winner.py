class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        has_c = [[False] * (len(nums) + 1) for i in range(len(nums) + 1)]
        c = [[None] * (len(nums) + 1) for i in range(len(nums) + 1)]

        def help(left, right):
            if left > right:
                return 0
            
            if has_c[left][right]:
                return c[left][right]
            
            s_left = nums[left] - help(left + 1, right)
            s_right = nums[right] - help(left, right - 1)

            has_c[left][right] = True
            c[left][right] = max(s_left, s_right)
            return c[left][right]

        return help(0, len(nums) -1) >= 0