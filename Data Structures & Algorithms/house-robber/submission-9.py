class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def max_amount(i: int) -> int:
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + max_amount(i+2), max_amount(i+1))

            return memo[i]
        
        return max_amount(0)
