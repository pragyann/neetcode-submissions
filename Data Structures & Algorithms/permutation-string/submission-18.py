class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_count, s2_count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        match = 0
        for i in range(26):
            match += 1 if s1_count[i] == s2_count[i] else 0
        
        l, r = 0, len(s1)

        while r < len(s2):
            if match == 26:
                return True
            
            to_remove = ord(s2[l]) - ord('a')
            if s2_count[to_remove] == s1_count[to_remove]:
                match -= 1
            s2_count[to_remove] -= 1
            if s2_count[to_remove] == s1_count[to_remove]:
                match += 1

            to_add = ord(s2[r]) - ord('a')
            if s2_count[to_add] == s1_count[to_add]:
                match -= 1
            s2_count[to_add] += 1
            if s2_count[to_add] == s1_count[to_add]:
                match += 1
            
            l +=1
            r += 1
        
        return match == 26
            