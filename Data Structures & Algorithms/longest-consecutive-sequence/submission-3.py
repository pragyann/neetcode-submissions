class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        res = 0

        for n in nums_set:
            if n-1 in nums_set:
                continue

            i = n+1
            seq_len = 1
            while i in nums_set:
                seq_len += 1
                i +=1 
            
            res = max(res, seq_len)
        
        return res


