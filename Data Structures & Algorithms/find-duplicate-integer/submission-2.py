class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] < 0:
                return abs(n)
            
            nums[abs(n) - 1] *= -1
        
        return -1
            


