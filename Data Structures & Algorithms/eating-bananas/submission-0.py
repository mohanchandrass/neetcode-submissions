class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1

        while(left<=right):
            mid = (left+right)//2
            count = 0
            for i in piles:
                r = (i + mid - 1)//mid
                count+=r
            
            if(count<=h):
                speed = mid
                right = mid - 1

            else:
                left = mid + 1

        return speed

            

                
        