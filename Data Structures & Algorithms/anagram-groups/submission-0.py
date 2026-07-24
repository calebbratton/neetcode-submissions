class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        result = []

        for s in strs:
            key = "".join(sorted(s))
            print(key)
            if key in seen:
                result[seen[key]].append(s)
            else:
                seen[key] = len(result)
                result.append([s])

        return result