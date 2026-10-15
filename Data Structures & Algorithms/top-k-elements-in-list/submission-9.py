class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        totes = Counter(nums)
        heap = []
        for (n, c) in totes.items():
            heapq.heappush(heap, (c, n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for (c, n) in heap:
            res.append(n)
        return res