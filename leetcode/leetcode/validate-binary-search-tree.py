# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def help(root, low, high):
            if not root: return True
            if root.val > low and root.val < high:
                return help(root.left, low, root.val) and help(root.right, root.val, high)
            return False 
        return help(root, float('-inf'), float('+inf'))