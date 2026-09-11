class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 

        # return self.binary_search_r(nums, l, r, target)
        return self.binary_search(nums, target)
    
    def binary_search_r(self, nums: List[int], l: int, r: int, target: int) -> int:
        if l <= r:
            mid = (l + r) // 2

            item = nums[mid]

            if item > target:
                return self.binary_search_r(nums, l, mid-1, target)
            elif item < target:
                return self.binary_search_r(nums, mid+1, r, target)
            else:
                return mid
        
        return -1

    def binary_search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r-l) // 2)

            item = nums[mid]

            if item < target:
                l = mid+1
            elif item > target:
                r = mid-1
            else:
                return mid
        
        return -1 
    
        