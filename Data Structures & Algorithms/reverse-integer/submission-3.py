class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = -1 if x<0 else 1
        x=abs(x)
        while x!=0:
            digit=(x%10)
            result =(result*10)+digit
            x//=10
            print(result)
        
        result*=sign
        if result<=-2**31 or result>= 2**31 - 1:
            return 0
    
        return result

            