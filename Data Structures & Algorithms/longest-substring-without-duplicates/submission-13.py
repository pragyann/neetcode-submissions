class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_set = set()

        l = 0
        res = 0
        for r in range(len(s)):

            while s[r] in seen_set:
                seen_set.remove(s[l])
                l += 1
            
            seen_set.add(s[r])
            res = max(r - l + 1, res)
        
        return res

            
