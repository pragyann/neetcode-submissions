class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 

        return self.binary_search(nums, l, r, target)
    
    def binary_search(self, nums: List[int], l: int, r: int, target: int) -> int:
        if l <= r:
            mid = (l + r) // 2

            item = nums[mid]

            if item > target:
                return self.binary_search(nums, l, mid-1, target)
            elif item < target:
                return self.binary_search(nums, mid+1, r, target)
            else:
                return mid
        
        return -1
        