from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = {
            (1,0),
            (-1,0),
            (0,-1),
            (0,1)
        }

        queue = deque()
        visited = set()
        fresh = 0


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    visited.add((i,j))
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh+=1
        
        
        time = 0
        while queue:     
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr = r+dr
                    nc = c+dc

                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and (nr,nc) not in visited:
                        if grid[nr][nc] == 1:
                            fresh-=1
                            grid[nr][nc] = 2
                            visited.add((nr,nc))
                            queue.append((nr,nc))
            if queue:
                time+=1


        return time if fresh==0 else -1

        