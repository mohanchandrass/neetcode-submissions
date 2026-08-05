class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a &= mask
        b &= mask
        while b:
            a,b = (a^b)&mask,((a&b)<<1)&mask

        if a & 0x80000000:
            a -= 1 << 32
        
        return a