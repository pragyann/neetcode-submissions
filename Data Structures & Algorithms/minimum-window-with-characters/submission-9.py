class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count_s = {}
        count_t = {}

        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        results, min_len = (-1, -1), float('inf')

        l = 0
        need, have = len(count_t), 0 

        for r, c in enumerate(s):
            count_s[c] = count_s.get(c, 0) + 1

            if c in count_t and count_s[c] == count_t[c]:
                have += 1
            
            while have == need:
                ss_length = r - l + 1
                if ss_length < min_len:
                    min_len = ss_length
                    results = (l, r)
                
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
            
        l, r = results

        if min_len == float('inf'):
            return ""
        
        return s[l:r+1]





