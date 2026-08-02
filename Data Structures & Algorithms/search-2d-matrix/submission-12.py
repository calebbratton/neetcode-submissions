class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = l + (r - l) // 2
            midRow = matrix[mid]
            minV, maxV = midRow[0], midRow[-1]

            if target >= minV and target <= maxV:
                foundIndex = self.binarySearch(midRow, target)
                return True if foundIndex > -1 else False
            elif target < minV:
                r = mid - 1
            else:
                l = mid + 1
        
        return False

    
    def binarySearch(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
