class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        longest = 0
        for num in sorted(nums):
            if num in seen:
                continue
            seen[num] = 1
            prev = num-1
            if prev in seen:
                seen[num] += seen[num-1]
            longest = max(longest, seen[num])
        return longest