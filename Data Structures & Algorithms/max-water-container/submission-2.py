class Solution:
    def maxArea(self, heights: List[int]) -> int:
        b1 = 0
        b2 = len(heights)-1

        maxarea = 0

        while b1<b2:
            area = (b2 - b1) * min(heights[b1],heights[b2])
            maxarea = max(maxarea,area)

            if heights[b1]<heights[b2]:
                b1+=1
            else:
                b2-=1
            
        return maxarea


            


        