class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [0] * len(nums), [0] * len(nums)

        for i, n in enumerate(nums):
            if i == 0:
                prefix[i] = n
                continue
            
            prefix[i] = prefix[i-1] * n
        
        for i in range(len(nums)-1, -1, -1):
            n = nums[i]
            if i == len(nums) - 1:
                suffix[i] = n
                continue
            
            suffix[i] = suffix[i+1] * n
        
        print(prefix, suffix)

        res = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0 :
                res[i] = suffix[1]
                continue
            if i == len(nums) - 1:
                res[i] = prefix[i - 1]
                continue
            res[i] = prefix[i-1] * suffix[i+1]
        
        return res
        