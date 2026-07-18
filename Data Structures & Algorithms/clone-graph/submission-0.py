"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        
        def dfs(node):
            if not node:
                return

            graph = Node(node.val)
        
            if node in visited:
                return visited[node]
                
            visited[node] = graph

            for neighbor in node.neighbors:
                graph.neighbors.append(dfs(neighbor))

            return graph
                    
        print(visited.values())

        return dfs(node)
        
        