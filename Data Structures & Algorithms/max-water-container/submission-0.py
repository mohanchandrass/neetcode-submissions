class Solution:
    def maxArea(self, heights: List[int]) -> int:
        b1 = 0
        b2 = len(heights)-1
        def formula(b1,b2):
            height = b2 - b1
            res = height * min(heights[b1],heights[b2])
            return res

        res = 0

        while b1<b2:
            check = formula(b1,b2)
            if check>res:
                res = check
                
            if heights[b1]<heights[b2]:
                b1+=1
            else:
                b2-=1
            

        
        return res


            


        