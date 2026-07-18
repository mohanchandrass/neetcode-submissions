class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        island = 0
        def dfs(row,col):
            visited.add((row,col))
            if row+1<len(grid) and grid[row+1][col]=="1" and (row+1,col) not in visited:
                dfs(row+1,col)
            if col+1<len(grid[0]) and grid[row][col+1]=="1" and (row,col+1) not in visited:
                dfs(row,col+1)
            if row-1>=0 and grid[row-1][col]=="1" and (row-1,col) not in visited:
                dfs(row-1,col)
            if col-1>=0 and grid[row][col-1]=="1" and (row,col-1) not in visited:
                dfs(row,col-1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=="1" and (row,col) not in visited:
                    dfs(row,col)
                    island+=1
                
        print(visited)
        return island
        

        