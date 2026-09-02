class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in seen:
                return [seen[diff], i + 1]
            seen[n] = i + 1
        return []
        