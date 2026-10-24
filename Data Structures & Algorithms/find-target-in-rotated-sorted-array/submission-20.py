class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(start, end) -> int:
            if start > end:
                return -1
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    return bs(start, mid - 1)
                return bs(mid + 1, end)
            else:
                if nums[mid] < target <= nums[end]:
                    return bs(mid + 1, end)
                return bs(start, mid - 1)

        return bs(0, len(nums)-1)