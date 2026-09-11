# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False

#         l, r = 0, len(s1) -1 
#         count = [0] * 26


#         while r < len(s2):
#             perm = s2[l:r+1]

#             count = [0] * 26
#             for i in range(len(s1)):
#                 count[ord(s1[i]) - ord('a')] += 1
#                 count[ord(perm[i]) - ord('a')] -= 1
            
#             exists = True
#             for freq in count:
#                 if freq != 0:
#                     exists=False
#                     break

#             if exists: return True

#             r += 1
#             l += 1

#         return False



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1_count[i] == s2_count[i] else 0)

        l = 0
        for r in range(len(s1)-1, len(s2)-1):
            if matches == 26:
                return True
            
            drop_index = ord(s2[l]) - ord('a')
            if s1_count[drop_index] == s2_count[drop_index]:
                matches -=1
            s2_count[drop_index] -= 1
            if s1_count[drop_index] == s2_count[drop_index]:
                matches +=1         

            add_index = ord(s2[r+1]) - ord('a')
            if s1_count[add_index] == s2_count[add_index]:
                matches -=1
            s2_count[add_index] += 1
            if s1_count[add_index] == s2_count[add_index]:
                matches +=1            

            l += 1
        
        return matches == 26
            





















