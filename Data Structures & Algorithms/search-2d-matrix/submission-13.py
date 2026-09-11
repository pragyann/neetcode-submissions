class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])

        for i in range(M):
            last_of_row = matrix[i][N-1]

            if target == last_of_row:
                return True
            elif target < last_of_row:
                return self.binary_search(matrix[i], target)
        
        return False
    
    def binary_search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            mid_elm = nums[m]

            if target < mid_elm:
                r = m-1
            elif target > mid_elm:
                l = m+1
            else:
                return True
        
        return False