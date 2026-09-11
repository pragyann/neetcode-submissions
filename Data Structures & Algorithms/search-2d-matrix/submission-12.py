class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])

        l, r = 0, (M*N) - 1

        while l <= r:
            mid = (l+r) // 2

            mid_elm = matrix[mid//N][mid%N]

            if target > mid_elm:
                l = mid + 1
            elif target < mid_elm:
                r = mid - 1
            else:
                return True
        
        return False