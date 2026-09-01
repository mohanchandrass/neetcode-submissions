from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = {
            (-1,0),
            (0,-1),
            (1,0),
            (0,1)
            
        }

        def bfs(queue):
            cells = set()
            
            while queue:
                for _ in range(len(queue)):
                    r,c = queue.popleft()
                    cells.add((r,c))
                    for dr,dc in directions:
                        nr,nc = r+dr,c+dc
                        if 0<=nr<len(heights) and 0<=nc<len(heights[0]) and (nr,nc) not in cells:
                            if heights[r][c]<=heights[nr][nc]:
                                cells.add((nr,nc))
                                queue.append((nr,nc)) 
            
            return cells

        
        pacific_queue = deque()
        atlantic_queue = deque()
        
        for i in range(len(heights)):
            pacific_queue.append((i,0))
            atlantic_queue.append((i,len(heights[0])-1))

        for j in range(len(heights[0])):
            pacific_queue.append((0,j))
            atlantic_queue.append((len(heights)-1,j))

        p_cells = bfs(pacific_queue)
        a_cells = bfs(atlantic_queue)
                
        res = p_cells & a_cells

        return list(res)