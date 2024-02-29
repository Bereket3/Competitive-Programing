# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def help(left_index, right_index):
            if left_index > right_index:
                return None
            middle_index = (left_index + right_index) // 2
            left_subtree = help(left_index, middle_index - 1)
            right_subtree = help(middle_index + 1, right_index)
            return TreeNode(nums[middle_index], left_subtree, right_subtree)
        return help(0, len(nums) - 1)