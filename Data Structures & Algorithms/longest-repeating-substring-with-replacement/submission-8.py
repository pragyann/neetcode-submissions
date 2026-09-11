class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        freq = {}
        res = 0
        max_f = 0

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_f = max(max_f, freq[s[r]])

            while (r-l+1) - max_f > k:
                freq[s[l]] -= 1
                l+= 1 

            res = max(res, (r-l+1))
            r+=1
        
        return res

            