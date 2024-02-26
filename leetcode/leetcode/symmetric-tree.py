class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def help(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and help(left.left, right.right) and help(left.right, right.left)
        return help(root.left, root.right)