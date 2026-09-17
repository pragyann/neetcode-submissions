# Bottom up approach
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1) # [0, 1, 2, 3, 4, 5]

        a, b = 1, 1

        for _ in range(n-1):
            temp = b
            b = a + b
            a = temp
        
        return b
