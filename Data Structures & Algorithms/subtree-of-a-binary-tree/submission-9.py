# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False          
            if sametree(p.left,q.left) is False or sametree(p.right,q.right) is False:
                return False
            
            return True

        def dfs(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val == q.val:
                if sametree(p,q) is False:
                    if dfs(p.right,q) is True or dfs(p.left,q) is True:
                        return True
                return sametree(p,q)
                
            if dfs(p.left,q) is True or dfs(p.right,q) is True:
                return True
            
            return False
        
        return dfs(root,subRoot)
            

        