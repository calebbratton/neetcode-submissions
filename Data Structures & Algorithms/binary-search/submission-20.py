class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binSearch(nums, target, 0, len(nums) - 1)

    def binSearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1

        mid = right - left // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binSearch(nums, target, left, mid - 1)
        else:
            return self.binSearch(nums, target, mid + 1, right)

        