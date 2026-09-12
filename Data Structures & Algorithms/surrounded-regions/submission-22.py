from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = {
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        }

        queue = deque()
        
        for row in range(0,len(board)):
            if board[row][0] == "O":
                board[row][0] = "S"
                queue.append((row,0))
            if board[row][len(board[0])-1] == "O":
                board[row][len(board[0])-1] = "S"
                queue.append((row,len(board[0])-1))
        
        for col in range(0,len(board[0])):
            if board[0][col] == "O":
                board[0][col] = "S"
                queue.append((0,col))
            if board[len(board)-1][col] == "O":
                board[len(board)-1][col] = "S"
                queue.append((len(board)-1,col))

        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr = dr+r
                    nc = dc+c      

                    if 0<=nr<len(board) and 0<=nc<len(board[0]):            
                        if board[nr][nc] == "O":
                            board[nr][nc] = "S"
                            queue.append((nr,nc))
            

        for row in range(0,len(board)):
            for col in range(0,len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "S":
                    board[row][col] = "O"
        

        return

                