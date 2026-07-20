class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*n

        if n >= 1:
            a = 1
            b = 1

        if n >= 2:
            b = 2

        for _ in range(2,n):
            a,b = b,a+b
        
        return b
        