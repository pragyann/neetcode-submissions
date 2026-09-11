class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for c in s:
            if c.isalnum():
                clean_s += c.lower()
                
        l, r = 0, len(clean_s) - 1 

        print(clean_s)

        while l <= r:
            if clean_s[l] != clean_s[r]:
                return False
            l += 1
            r -= 1
        
        return True