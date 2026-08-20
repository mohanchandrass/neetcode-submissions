# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def dfs(node):
            lr,rr=None,None
            nonlocal count
            if not node:
                return 

            lr = dfs(node.left)

            if lr is not None:
                return lr

            count+=1
            print(node.val,count)
            
            if count==k:
                return node.val
            rr = dfs(node.right)

            if rr is not None:
                return rr

            return lr if lr else rr

        return dfs(root)
        