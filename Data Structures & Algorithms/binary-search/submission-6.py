class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.recurse(nums, 0, len(nums) - 1, target)

    def recurse(self, nums, l, r, target):
        if l > r:
            return -1
        
        mid = l + (r - l) // 2

        if target > nums[mid]:
            return self.recurse(nums, mid + 1, r, target)
        elif target < nums[mid]:
            return self.recurse(nums, l, mid - 1, target)
        return mid
