class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [{},{},{}]
        for i in range(len(board)):
            rows = {}
            cols = {}
            if (i)%3==0:
                boxes = [{},{},{}]
            
            for j in range(len(board)):

                if board[i][j]!='.':
                    #row
                    if board[i][j] in rows:
                        return False
                    rows[board[i][j]] = 1
                    #box
                    if board[i][j] in boxes[j//3]:
                        return False
                    boxes[j//3][board[i][j]] = 1

                if board[j][i]!='.':
                    #col
                    if board[j][i] in cols:
                        return False
                    cols[board[j][i]] = 1
                            
        return True




        