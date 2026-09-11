class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for n in nums:
            if n-1 in nums_set:
                continue
            
            length, p = 0, n
            while p in nums_set:
                length += 1
                p += 1
            
            res = max(res, length)
        
        return res