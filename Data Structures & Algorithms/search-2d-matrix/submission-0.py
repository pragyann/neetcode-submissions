class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_flat = []

        for row in matrix:
            matrix_flat.extend(row)

        return self.binarySearch(matrix_flat, 0, len(matrix_flat) - 1, target) != -1

    
    def binarySearch(self, nums, l, r, target):
        if l > r:
            return -1
        
        mid = l + (r-l) // 2

        if target < nums[mid]:
            return self.binarySearch(nums, l, mid-1, target)
        elif target > nums[mid]:
            return self.binarySearch(nums, mid+1, r, target)
        else:
             return mid
