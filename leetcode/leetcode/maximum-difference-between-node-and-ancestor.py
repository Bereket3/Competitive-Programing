class Solution:
    def maxAncestorDiff(self, r: Optional[TreeNode]) -> int:
        def help(root, max_, min_):
            if root:
                max_, min_ = max(max_, root.val), min(min_, root.val)
                return max(help(root.left, max_, min_), help(root.right, max_, min_))
            else:
                return max_ - min_
        return help(r, r.val, r.val)