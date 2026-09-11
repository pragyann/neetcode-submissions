class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_to_search = []

        for row in matrix:
            l, r = 0, len(row) - 1
            if target >= row[l] and target <= row[r]:
                row_to_search = row
                break

        return self.binarySearch(row_to_search, 0, len(row_to_search) - 1, target) != -1
    
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
        



