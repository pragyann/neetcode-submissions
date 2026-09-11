class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) -1 

        while r < len(s2):
            perm = s2[l:r+1]

            count = [0] * 26
            for i in range(len(s1)):
                count[ord(s1[i]) - ord('a')] += 1
                count[ord(perm[i]) - ord('a')] -= 1
            print(count)
            
            exists = True
            for freq in count:
                if freq != 0:
                    exists=False
                    break
            print(exists)
            if exists: return True

            r += 1
            l += 1

            
        return False