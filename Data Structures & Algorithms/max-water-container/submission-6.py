class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            maxHeight = min(heights[l], heights[r])
            area = (r - l) * maxHeight
            res = max(res, area)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return res