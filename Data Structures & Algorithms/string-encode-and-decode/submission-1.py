class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        length_str = ""
        for s in strs:
            length_str += str(len(s)) + '_'

        return f"{length_str}#{"".join(strs)}"


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        sep_index = 0
        for i,c in enumerate(s):
            if c == '#':
                sep_index = i
                break
        length_str = s[0:sep_index-1] # -1 to get rid of the last _
        msg_str = s[sep_index+1:]

        lengths = [int(l) for l in length_str.split("_")]

        strs = []
        i = 0
        for l in lengths:
            print(l)
            strs.append(msg_str[i:i+l])
            i += l
        return strs
