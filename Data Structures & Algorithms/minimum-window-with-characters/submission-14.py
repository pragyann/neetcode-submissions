class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count_s = {}
        count_t = {}

        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        l = 0 
        res, min_len = [0, 0], float('inf')

        have, need = 0, len(count_t)

        for r in range(len(s)):
            c = s[r]
            count_s[c] = count_s.get(c, 0) + 1

            if c in count_t and count_t[c] == count_s[c]:
                have += 1

            while need == have:
                curr_len = r - l + 1
                if curr_len < min_len:
                    min_len = curr_len
                    res = [l, r]
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        return s[l:r+1] if min_len != float('inf') else ""
            
