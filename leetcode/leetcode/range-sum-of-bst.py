# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
            out = []
            def help(root):
                if root:
                    help(root.left)
                    out.append(root.val)
                    help(root.right)
            help(root)
            return out
        
        out = inorderTraversal(root)
        res = 0
        for i in out:
            if i >= low and i <= high:
                res += i
        return res