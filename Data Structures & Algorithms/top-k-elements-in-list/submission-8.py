class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [k for (k, v) in sorted(Counter(nums).items(), key= lambda i: i[1], reverse=True)][:k]