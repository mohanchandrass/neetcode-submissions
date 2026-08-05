class Solution:
    def reverseBits(self, n: int) -> int:
        res=""
        for i in range(32):
            num = n>>i
            res+=str(num&1)
            print(res)
        
        res = int(res,2)
        
        return res
            
            

            
            
            

        