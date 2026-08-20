# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxval = float("inf")
        minval = -float("inf")
        def dfs(node,maxval,minval):
            if node is None:
                return True
            
            if node.val<=minval or node.val>=maxval:
                return False
            
            
            res = dfs(node.left,node.val,minval) 

            res2 = dfs(node.right,maxval,node.val)

            return (res and res2)
        
        return dfs(root,maxval,minval)
        