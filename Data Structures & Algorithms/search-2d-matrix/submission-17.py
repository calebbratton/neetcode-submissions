class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        n = (rows*cols) - 1
        l, r = 0, n
        while l <= r:
            mid = (r + l) // 2
            row,col = mid // cols, mid % cols
            v = matrix[row][col]
            if v < target:
                l = mid + 1
            elif v > target:
                r = mid - 1
            else:
                return True
        return False