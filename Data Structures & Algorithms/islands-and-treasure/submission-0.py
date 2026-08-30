from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        directions = {
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        }

        queue = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))

       
        distance = 1
        while len(queue)!=0:
            size = len(queue)
            for _ in range(size):
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr = r+dr
                    nc = c+dc

                    if (nr,nc) not in visited and 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                        if grid[nr][nc] == 2147483647:
                            grid[nr][nc] = distance
                            visited.add((nr,nc))
                            queue.append((nr,nc))
            
            distance+=1


        return