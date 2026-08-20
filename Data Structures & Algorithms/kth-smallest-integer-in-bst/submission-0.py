# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                return True
            if node.left:
                dfs(node.left)
            res.append(node.val)
            if node.right:
                dfs(node.right)

            return True
        
        dfs(root)
        
        return res[k-1]
        