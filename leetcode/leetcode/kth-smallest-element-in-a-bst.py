# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        out = []
        def help(root):
            if root:
                help(root.left)
                out.append(root.val)
                help(root.right)
        help(root)
        return out[k-1]