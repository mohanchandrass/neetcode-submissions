# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def bfs(node):
            if node is None:
                return
            queue = deque([node])

            while queue:
                n = len(queue)

                result.append([node.val for node in queue])
                
                while n!=0:
                    node = queue.popleft()

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

                    n-=1


        bfs(root)

        return result


        