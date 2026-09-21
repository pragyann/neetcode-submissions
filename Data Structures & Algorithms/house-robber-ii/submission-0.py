class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        a, b = 0, 0

        for i in range(len(nums)):
            b, a = max(nums[i] + a, b), b
        
        return b