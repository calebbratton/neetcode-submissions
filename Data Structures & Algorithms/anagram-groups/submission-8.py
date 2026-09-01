class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            keyed = "".join(sorted(s))
            if keyed not in groups:
                groups[keyed] = []
            groups[keyed].append(s)
        return list(groups.values())
        