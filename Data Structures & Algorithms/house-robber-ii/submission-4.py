class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        front, back = nums[:n - 1], nums[1:]
        def steal(houses):
            prev, neighbor = 0, 0
            for h in houses:
                curr = max(h + prev, neighbor)
                prev = neighbor
                neighbor = curr
            return neighbor
        return max(steal(front), steal(back))
            
            