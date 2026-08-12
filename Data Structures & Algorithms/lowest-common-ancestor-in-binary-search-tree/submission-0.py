# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):            
            if p.val<=node.val and node.val<=q.val or q.val<=node.val and node.val<=p.val :
                return node
            if p.val<node.val and q.val<node.val:
                return dfs(node.left)
            if p.val>node.val and q.val>node.val:
                return dfs(node.right)
            
        return dfs(root)

        