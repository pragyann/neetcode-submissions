class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()

        l, r = 0, 0
        res = 0

        while r < len(s):

            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            length = r - l +1
            res = max(res, length)
            window.add(s[r])
            r += 1

        return res