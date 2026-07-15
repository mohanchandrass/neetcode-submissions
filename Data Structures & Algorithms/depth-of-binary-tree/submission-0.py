# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            d_left = dfs(node.left)
            d_right = dfs(node.right)
            
            return 1 + max(d_left, d_right)

        return dfs(root)
        
 
            
            
        
        
        