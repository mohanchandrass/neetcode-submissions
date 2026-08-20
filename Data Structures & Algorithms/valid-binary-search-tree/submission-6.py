# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,maxval,minval):
            if node is None:
                return True
            
            if node.val<=minval or node.val>=maxval:
                return False

            return dfs(node.left,node.val,minval) and dfs(node.right,maxval,node.val)
        
        return dfs(root, float("inf"),-float("inf"))
        