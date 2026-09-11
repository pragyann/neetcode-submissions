class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_to_search = self.binarySearchRow(matrix, 0, len(matrix)-1,  target)

        return self.binarySearch(row_to_search, 0, len(row_to_search) - 1, target) != -1
    
    def binarySearchRow(self, matrix, t, b, target):
        if t > b:
            return []
        
        m = (t + b) // 2

        row = matrix[m]

        if target < row[0]:
            return self.binarySearchRow(matrix, t, m - 1, target)
        elif target > row[-1]: 
            return self.binarySearchRow(matrix, m + 1, b, target)
        else:
             return row
    
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
        



