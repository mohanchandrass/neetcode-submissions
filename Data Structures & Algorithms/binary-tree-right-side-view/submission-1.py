# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if root is None:
            return result

        queue = deque([root])

        while queue:
            n = len(queue)
            result.append(queue[-1].val)
            print(result)

            while n!=0:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                n-=1
        
        return result
        




            

        