class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += f"{len(s)}#{s}"
        
        return res # "5#Hello5#World"

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            length = int(length)
            i += 1
            res.append(s[i: i + length])

            i += length
        
        return res





            

