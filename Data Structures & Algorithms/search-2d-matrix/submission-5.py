class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1

        while r < m and c >= 0:
            value = matrix[r][c]

            if target < value:
                c -= 1
            elif target > value:
                r += 1
            else:
                return True
        
        return False