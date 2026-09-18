class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def get_max(start: int, end: int) -> int:
            if start == end: # only 1 elem remaining
                return nums[start]
            if end == start + 1: # only 2 elem remaining
                return max(nums[start], nums[end])
            
            res = 0

            if (start,end) in memo:
                return memo[(start,end)]

            for i in range(start, end+1):
                curr_max = nums[i]

                left = get_max(start, i-2) if i-2 >= 0 else 0
                right = get_max(i+2, end) if i+2 <len(nums) else 0

                res = max(res, curr_max + left + right)    

            memo[(start,end)] = res

            return res

        return get_max(0, len(nums) - 1)