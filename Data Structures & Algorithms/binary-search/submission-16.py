class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.find(nums, target, 0, len(nums)-1)
        

    def find(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1

        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.find(nums, target, left, mid - 1)

        return self.find(nums, target, mid + 1, right)
