# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        if not root:
            return out
        
        queue = deque([root])

        to_right = True

        while queue:
            ans = []
            for i in range(len(queue)):
                node = queue.popleft()
                ans.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if to_right:
                out.append(ans)
            else:
                out.append(ans[::-1])
            
            to_right = not to_right

        return out