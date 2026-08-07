# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if p is None and q is None:
                return True           
            if p is None or q is None:
                return False
            if p.val!=q.val:
                return False

            if dfs(p.left,q.left) is False or dfs(p.right,q.right) is False:
                return False
            
            return True

        return dfs(p,q)
        