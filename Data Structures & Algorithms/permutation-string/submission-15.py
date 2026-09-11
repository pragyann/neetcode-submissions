class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1, count_s2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1

        l, r = 0, len(s1) - 1

        while r < len(s2):
            match = 0
            for i in range(26):
                match += 1 if count_s1[i] == count_s2[i] else 0

            if match == 26:
                return True
            count_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            if r < len(s2):
                count_s2[ord(s2[r]) - ord('a')] += 1

        return False

