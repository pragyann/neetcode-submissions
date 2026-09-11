class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}

        l = 0
        res = 0

        max_len = 0

        for r in range(len(s)):
            c = s[r]
            freq_map[c] = freq_map.get(c, 0) + 1
            max_len = max(max_len, freq_map[c])

            while (r-l+1) > max_len + k and l < r:
                freq_map[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)

        return res
