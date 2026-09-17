class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def ways_to_climb(step: int) -> int:
            if step == n:
                return 1
            if step > n:
                return 0
            
            if step in memo:
                return memo[step]

            memo[step] = ways_to_climb(step + 1) + ways_to_climb(step + 2)    
            return memo[step]

        return ways_to_climb(0)