# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
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
        c = Counter(out)
        k = []
        _max_f = float('-inf')
        for i in c:
            _max_f = max(_max_f, c[i])

        for i, j in c.items():
            if j == _max_f:
                k.append(i)

        return k