class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        l, r = 0, len(s1) - 1
        count_1 = [0] * 26
        for c in s1:
            count_1[ord(c) - ord('a')] += 1

        while r < len(s2):
            count_2 = [0] * 26
            for j in range(l, r+1):
                count_2[ord(s2[j]) - ord('a')] += 1            

            match = True
            for i in range(26):
                if count_1[i] != count_2[i]:
                    match = False
                    break

            if match: 
                return True
            l+=1
            r+=1
        
        return False


