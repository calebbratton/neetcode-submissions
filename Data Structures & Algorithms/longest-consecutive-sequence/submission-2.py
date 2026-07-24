class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = sorted(set(nums))

        print(numSet)
        longest = 0
        current = 0
        for i, num in enumerate(numSet):
            if i == 0:
                current+=1
                longest+=1
            elif numSet[i-1]+1 == num:
                current+=1
                longest = max(current, longest)
            else:
                current = 1 
            print(longest, current)



        return longest
        