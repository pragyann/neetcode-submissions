class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1, count_s2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1

        l, r = 0, len(s1) # l points to char to remove and r points to char to add

        match = 0
        for i in range(26):
            match += 1 if count_s1[i] == count_s2[i] else 0

        while r < len(s2):
            if match == 26:
                return True
            
            to_remove = ord(s2[l]) - ord('a')
            if count_s1[to_remove] == count_s2[to_remove]:
                match -= 1
            count_s2[to_remove] -= 1
            if count_s1[to_remove] == count_s2[to_remove]:
                match += 1

            to_add = ord(s2[r]) - ord('a')
            if count_s1[to_add] == count_s2[to_add]:
                match -= 1
            count_s2[to_add] += 1
            if count_s1[to_add] == count_s2[to_add]:
                match += 1

            l += 1
            r += 1


        return match == 26 

