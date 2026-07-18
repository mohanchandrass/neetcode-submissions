class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        area = 0
        def dfs(row,col):
            nonlocal area
            area+=1
            grid[row][col] = 0
            if row+1<len(grid) and grid[row+1][col] == 1:
                dfs(row+1,col)      
            if col+1<len(grid[0]) and grid[row][col+1] == 1:
                dfs(row,col+1)
            if row-1>=0 and grid[row-1][col] == 1:
                dfs(row-1,col)
            if col-1>=0 and grid[row][col-1] == 1:
                dfs(row,col-1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(row,col)
                    maxarea = max(maxarea,area)
                    area = 0
        
        return maxarea

        