class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count_1 = [0] * 26
        count_2 = [0] * 26

        for i in range(len(s1)):
            count_1[ord(s1[i]) - ord('a')] += 1
            count_2[ord(s2[i]) - ord('a')] += 1
        
        match = 0
        for i in range(26):
            match += 1 if count_1[i] == count_2[i] else 0
        
        l, r = 0, len(s1)

        while r < len(s2):
            if match == 26:
                return True

            to_drop = ord(s2[l]) - ord('a')
            if count_1[to_drop] == count_2[to_drop]:
                match -= 1
            count_2[to_drop] -=1
            if count_1[to_drop] == count_2[to_drop]:
                match += 1


            to_add = ord(s2[r]) - ord('a')
            if count_1[to_add] == count_2[to_add]:
                match -= 1
            count_2[to_add] += 1
            if count_1[to_add] == count_2[to_add]:
                match += 1

            l+=1
            r+=1
        
        return match == 26
