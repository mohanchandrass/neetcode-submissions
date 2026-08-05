class Solution:
    def reverseBits(self, n: int) -> int:
        res=""
        num = 0
        for i in range(32):
            num<<=1
            num|=((n>>i)&1)
        
        return num
            
            

            
            
            

        