class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "%" + s
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        print(s)
        while i < len(s):
            num = ""
            if i > 0 and s[i] == '%' and s[i-1].isnumeric():
                j = i-1
                while j >= 0 and s[j].isnumeric():
                    num = s[j] + num
                    j -= 1
                nint = int(num)
                start = i + 1
                end = i + nint +1
                res.append(s[start: end])
                s = s[end:]
                i = 0
            else:
                i+=1
        return res
