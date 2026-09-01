class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for n in nums:
            seen[n] += 1
        
        return [n for n, c in heapq.nlargest(k, list(seen.items()), key = lambda i: i[1])]
        