class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def recurse(start: int, end: int) -> int:
            if start == end:
                return nums[start]
            if end == start + 1:
                return max(nums[start], nums[end])
            
            if (start, end) in memo:
                return memo[(start,end)]

            res = 0

            for i in range(start, end+1):

                left = recurse(start, i-2) if i-2 >=0 else 0
                right = recurse(i+2, end) if i+2 <len(nums) else 0

                res = max(res, nums[i] + left + right)
            
            memo[(start, end)] = res
            return res
        
        return recurse(0, len(nums) - 1)