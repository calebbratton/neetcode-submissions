class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (-count[num], num))

        res = []
        for i in range(k): 
            v = heapq.heappop(heap)[1]
            res.append(v)

        return res