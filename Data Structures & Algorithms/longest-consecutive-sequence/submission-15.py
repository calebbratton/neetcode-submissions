class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = defaultdict(int)
        longest = 0
        nums.sort()
        for num in nums:
            print(num)
            seq[num] = 1
            if num-1 in seq:
                seq[num] += seq[num-1]
            longest = max(longest, seq[num])
        return longest