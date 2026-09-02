class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        current = []
        longest = []
        for num in sorted(set(nums)):
            if current:
                if num - current[-1] != 1:
                    current = []
            current.append(num)
            if len(current) > len(longest):
                longest = current
        return len(longest)