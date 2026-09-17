# bottom up, optimal
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # a, b = cost[n-2], cost[n-1]

        for step in range(n-3, -1, -1):
            # a, b = cost[step] + min(a, b), a
            cost[step] = cost[step] + (min(cost[step+1], cost[step+2]))
        
        return min(cost[0], cost[1])