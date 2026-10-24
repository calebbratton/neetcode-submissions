class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(l, r) -> int:
            if r < l:
                return -1
            m = (r + l) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    return bs(l, m - 1)
                return bs(m + 1, r)
            else:
                if nums[m] < target <= nums[r]:
                    return bs(m + 1, r)
                return bs(l, m - 1)

        return bs(0, len(nums)-1)