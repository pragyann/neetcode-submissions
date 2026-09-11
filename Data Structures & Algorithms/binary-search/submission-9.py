class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.recurse(nums, 0, len(nums) - 1, target)
    
    def recurse(self, nums: List[int], l:int, r:int, target: int) -> int:
        if l > r:
            return -1
            
        mid = (l+r) // 2
        mid_elm = nums[mid]

        if target < mid_elm:
            return self.recurse(nums, l, mid-1, target)
        elif target > mid_elm:
            return self.recurse(nums, mid+1, r, target)
        elif target == mid_elm:
            return mid
        
