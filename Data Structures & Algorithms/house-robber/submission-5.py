class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def max_money(i: int) -> int:
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]
            
            memo[i] =  max(max_money(i+1), nums[i] + max_money(i+2))

            return memo[i]
        
        return max_money(0)

