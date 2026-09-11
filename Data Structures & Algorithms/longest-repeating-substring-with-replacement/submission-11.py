class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}

        l = 0
        res = 0

        max_f = 0

        for r in range(len(s)):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            max_f = max(max_f, freq_map[s[r]])

            while (r-l+1) - max_f > k:
                freq_map[s[l]] -= 1
                l += 1

                # no need to decrease max_f as res won't change
                # res changes only when max_f was increased

            res = max(res, r-l+1)

        return res
