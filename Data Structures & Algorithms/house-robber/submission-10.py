class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0

        for i in range(len(nums)):
            b, a = max(nums[i] + a, b), b
        
        return b

        # def max_amount(i: int) -> int:
        #     if i >= len(nums):
        #         return 0

        #     if i in memo:
        #         return memo[i]

        #     memo[i] = max(nums[i] + max_amount(i+2), max_amount(i+1))

        #     return memo[i]
        
        # return max_amount(0)
