class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def minCost(step: int) -> int:
            if step >= len(cost):
                return 0
            
            if step in memo:
                return memo[step]
            
            memo[step] = cost[step] + min(minCost(step + 1), minCost(step + 2))
            return memo[step]
        
        return min(minCost(0), minCost(1))