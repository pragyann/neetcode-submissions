# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if len(t) > len(s):
#             return ""

#         min_ss = ""

#         # l,r = 0, len(t) - 1
#         l, r = 0, 0

#         t_count = defaultdict(int)
#         for c in t:
#             t_count[c] = t_count.get(c, 0) + 1
        
#         s_count = defaultdict(int)
#         if s[r] in t_count:
#             s_count[s[r]] = 1

#         while r < len(s):
#             is_curr_window_substring = True
#             for c in t:
#                 if t_count[c] > s_count[c]:
#                     is_curr_window_substring = False
#                     break

#             if is_curr_window_substring: 
#                 ss = s[l:r+1]
#                 if len(ss) < len(min_ss) or min_ss == "":
#                     min_ss = ss
                
#                 if s[l] in t_count:
#                     s_count[s[l]] -= 1
#                 l += 1
#             else:
#                 r += 1
#                 if r < len(s) and s[r] in t_count:
#                     s_count[s[r]] += 1
        
#         return min_ss

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""

        s_count = {}
        t_count = {}

        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        
        have, need = 0, len(t_count)
        res, resLen = [-1, -1], float('inf')
        l = 0
        
        for r in range(len(s)):
            s_count[s[r]] = s_count.get(s[r], 0) + 1

            if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
                have += 1

            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1

                l += 1
        print(res)
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""




        