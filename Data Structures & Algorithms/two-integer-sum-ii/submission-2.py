class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(numbers):
            current_sum = target - num
            if current_sum in seen:
                return [seen[current_sum], i+1]
            else:
                seen[num] = i+1
        return []
        