class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)-1
        memo = {}
        if n>=1:
            memo[0] = cost[0]
            memo[1] = cost[1] 
    

        def climb(n):
            if n in memo:
                return memo[n]

            memo[n] = cost[n] + min(climb(n-1),climb(n-2))

            return memo[n]
            
        
        return min(climb(n),climb(n-1))

        