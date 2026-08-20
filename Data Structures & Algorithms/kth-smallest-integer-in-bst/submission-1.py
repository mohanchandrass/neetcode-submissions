# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        lr = -1
        rr = -1
        def dfs(node):
            nonlocal count,lr,rr
            if not node:
                return -1
            if node.left:
                lr = dfs(node.left)
            count+=1
            print(node.val,count)
            if count==k:
                return node.val
    
            if node.right:
                rr = dfs(node.right)

            if lr!=-1:
                return lr
            
            if rr!=-1:
                return rr


            return lr if lr else rr

        return dfs(root)
        