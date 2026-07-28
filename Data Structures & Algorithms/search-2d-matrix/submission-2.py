class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        if len(matrix) == 1:
            return target in matrix[0]
        midMatrix = len(matrix) // 2

        currentRow = matrix[midMatrix]
        if target < currentRow[0]:
            return self.searchMatrix(matrix[:midMatrix], target)
        elif target > currentRow[-1]:
            return self.searchMatrix(matrix[midMatrix::], target)
        else:
            return self.searchMatrix([currentRow], target)
        