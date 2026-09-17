class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n # [0, 1, 2, n-1,]
        dp[n-1] = cost[n-1]
        dp[n-2] = cost[n-2]

        for step in range(n-3, -1, -1):
            dp[step] = cost[step] + min(dp[step+1], dp[step+2])
        
        return min(dp[0], dp[1])