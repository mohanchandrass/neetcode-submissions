class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)+1))
        size = [1]*(len(edges)+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(a,b):
            ra = find(a)
            rb = find(b)

            if ra == rb:
                return False
            
            if size[ra]<size[rb]:
                ra,rb = rb,ra

            parent[rb] = ra

            size[ra]+=size[rb]
            
            return True
        
        for a,b in edges:
            if union(a,b) == False:
                return [a,b]

        
        