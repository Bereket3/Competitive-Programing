# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def help(root, _sum):
            if not root:
                return 0
            
            _sum = _sum*10 + root.val

            if not root.left and not root.right:
                return _sum
            
            return help(root.left, _sum) + help(root.right, _sum)

        return help(root, 0)