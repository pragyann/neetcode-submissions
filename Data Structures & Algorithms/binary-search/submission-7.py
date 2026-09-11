class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            mid_element = nums[m]

            if target > mid_element:
                l = m+1
            elif target < mid_element:
                r = m-1
            else:
                return m
        
        return -1
        