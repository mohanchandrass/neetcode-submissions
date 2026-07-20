class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) - 1

        if n<=2:
            return cost[n-1]

        a = cost[0]
        b = cost[1]

        for i in range(2,n+1):
            a,b = b,(cost[i]+min(a,b))
            print(a,b)
        
        return min(a,b)


        