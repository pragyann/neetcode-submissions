class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        n = len(cost)
        def minCost(i: int) -> int:
            if i == n - 2 or i == n-1:
                return cost[i]
            
            if i in memo: return memo[i]

            memo[i] = cost[i] + min(minCost(i+1), minCost(i+2))         
            return memo[i]

        return min(minCost(0), minCost(1))