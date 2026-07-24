class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elms = defaultdict(int)
        for num in nums:
            elms[num]+=1

        return sorted(elms.keys(), key=lambda n: elms[n], reverse=True)[:k]