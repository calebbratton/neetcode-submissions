class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        result = []

        for i, s in enumerate(strs):
            skey = ''.join(sorted(s))
            sindex = seen.get(skey)
            if skey in seen:
                result[sindex].append(s)
            else:
                seen[skey] = len(result)
                result.append([s])
        return result

        