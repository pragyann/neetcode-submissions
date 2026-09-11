class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        total = m * n
        l, r = 0, total-1

        while l <= r:
            mid = l + (r - l) // 2

            row = mid // n
            col = mid % n

            item = matrix[row][col]

            if target < item:
                r = mid - 1
            elif target > item:
                l = mid + 1
            else:
                return True
        
        return False
