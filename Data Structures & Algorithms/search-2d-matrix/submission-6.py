class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lRow, rRow = 0, len(matrix) - 1

        while lRow <= rRow:
            midRowIndex = lRow + (rRow - lRow // 2)
            midRow = matrix[midRowIndex]
            minV, maxV = midRow[0], midRow[len(midRow) - 1]
            print(minV, maxV, target)

            if target >= minV and target <= maxV:
                return self.binSearch(midRow, target)
            elif target < minV:
                rRow = midRowIndex - 1
            else:
                lRow = midRowIndex + 1
        
        return False

    def binSearch(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r - l // 2)
            c = nums[mid]

            if c == target:
                return True
            elif c > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False