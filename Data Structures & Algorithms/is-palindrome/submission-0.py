class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        clean_s = ""
        for c in s:
            if self.isAlphanumeric(c):
                clean_s += c
        
        l, r = 0, len(clean_s)-1

        while l < r:
            if clean_s[l] != clean_s[r]:
                return False
            l += 1
            r -= 1
        
        return True
    
    def isAlphanumeric(self, c: str) -> bool:
        return (c >= '0' and c <='9') or (c >= 'a' and c <='z')
