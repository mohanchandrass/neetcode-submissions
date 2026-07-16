# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        diff = 0

        def dfs(node):
            nonlocal balanced,diff
            if not node:
                return 0
            d_l = dfs(node.left)
            d_r = dfs(node.right)
        
            if abs(d_l-d_r)>1:
                balanced = False

            
            return 1+max(d_l,d_r)
        
        dfs(root)

        return balanced

