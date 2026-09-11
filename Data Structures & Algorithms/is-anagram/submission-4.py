class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_array = [0] * 26

        for i in range(len(s)):
            freq_array[ord(s[i]) - ord('a')] += 1
            freq_array[ord(t[i]) - ord('a')] -= 1
        
        for freq in freq_array:
            if freq !=0:
                return False
        
        return True