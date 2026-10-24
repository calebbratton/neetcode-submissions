class Solution:
    def findMin(self, nums: List[int]) -> int:
        def search(start:int, end:int) -> int:
            if start == end:
                return nums[start]
            m = start + (end - start) // 2
            if nums[m] > nums[end]:
                return search(m+1, end)
            return search(start, m)
        return search(0, len(nums)-1)