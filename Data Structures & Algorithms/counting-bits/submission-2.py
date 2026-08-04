class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        memo = {}
        def check(x):
            nonlocal count
            if x == 0:
                return 0
            if x in memo:
                return memo[x]
            x&=(x-1)
            count+=1
            check(x)
            return count
            
        for i in range(n+1):
            count = 0
            result.append(check(i))


        return result

