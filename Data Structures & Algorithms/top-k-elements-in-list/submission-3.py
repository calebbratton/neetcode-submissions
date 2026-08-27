class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))

        return [v[1] for v in heapq.nlargest(k, heap)]