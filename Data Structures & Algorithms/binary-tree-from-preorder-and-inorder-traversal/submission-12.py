# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        rpos = 0
        inorder_pos = {}

        for i,val in enumerate(inorder):
            inorder_pos[val] = i    

        def buildbt(left,right):
            nonlocal rpos
            if left > right:
                return None

            node = TreeNode(preorder[rpos])
            rpos+=1

            pos = inorder_pos[node.val]

            node.left = buildbt(left,pos-1)
            node.right = buildbt(pos+1,right)

            return node
         

        return buildbt(0,len(inorder)-1)                   
            

                

        