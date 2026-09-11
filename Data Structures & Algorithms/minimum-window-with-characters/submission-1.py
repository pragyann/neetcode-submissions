class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        min_ss = ""

        l,r = 0, len(t) - 1

        t_count = defaultdict(int)
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        
        s_count = defaultdict(int)
        for i in range(l, r+1):
            s_count[s[i]] = s_count.get(s[i], 0) + 1

        while r < len(s):
            print(s_count)
            is_curr_window_substring = True
            for c in t:
                if t_count[c] > s_count[c]:
                    is_curr_window_substring = False
                    break

            print(s[l:r+1], is_curr_window_substring)

            if is_curr_window_substring: 
                ss = s[l:r+1]
                if len(ss) < len(min_ss) or min_ss == "":
                    min_ss = ss
                
                s_count[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r < len(s):
                    s_count[s[r]] += 1
        
        return min_ss
        