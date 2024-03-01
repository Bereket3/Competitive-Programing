# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def help(nums):
            if nums.__len__() == 1:
                return TreeNode(nums[0])
            
            max_ = 0

            for i in range(len(nums)):
                if nums[max_] < nums[i]:
                    max_ = i
                
            new = TreeNode(nums[max_])

            if max_ == len(nums) - 1:
                new.left = help(nums[:max_])
                return new
            elif max_ == 0:
                new.right = help(nums[1:])
                return new
            else:
                new.left = help(nums[:max_])
                new.right = help(nums[max_ + 1:])
                return new
        return help(nums)