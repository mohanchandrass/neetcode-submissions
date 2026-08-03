class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        row = len(matrix)
        col = len(matrix[0])
        top = 0
        bottom = row-1
        left = 0
        right = col-1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1
            if top>bottom:
                break
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right-=1
            if right<left:
                break
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom-=1
            if bottom<top:
                break
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
            left+=1
        
        return result

        

    
            
            
            
            
                
        