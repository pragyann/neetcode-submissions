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



# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False
        
#         s1_count = [0] * 26
#         s2_count = [0] * 26

#         for i in range(len(s1)):
#             s1_count[ord(s1[i]) - ord('a')] += 1
#             s2_count[ord(s2[i]) - ord('a')] += 1
        
#         matches = 0
#         for i in range(26):
#             matches += (1 if s1_count[i] == s2_count[i] else 0)

#         l = 0
#         for r in range(len(s1)-1, len(s2)-1):
#             if matches == 26:
#                 return True
            
#             drop_index = ord(s2[l]) - ord('a')
#             # If it was equal before, we distrubed a match
#             if s1_count[drop_index] == s2_count[drop_index]:
#                 matches -=1
#             s2_count[drop_index] -= 1
#             # If it is equal after, we created a match
#             if s1_count[drop_index] == s2_count[drop_index]:
#                 matches +=1         

#             add_index = ord(s2[r+1]) - ord('a')
#             # If it was equal before, we distrubed a match
#             if s1_count[add_index] == s2_count[add_index]:
#                 matches -=1
#             s2_count[add_index] += 1
#             # If it is equal after, we created a match
#             if s1_count[add_index] == s2_count[add_index]:
#                 matches +=1            

#             l += 1
        
#         return matches == 26
            
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False

#         s1_count = [0] * 26
#         s2_count = [0] * 26

#         for i in range(len(s1)):
#             s1_count[ord(s1[i])-ord('a')] += 1
#             s2_count[ord(s2[i])-ord('a')] += 1

#         matches = 0
#         for i in range(26):
#             matches += (1 if s1_count[i] == s2_count[i] else 0)
        
#         # l = index of element outside, left to the window
#         # r = index of element outside, right to the window
#         l = 0
#         for r in range(len(s1), len(s2)):
#             if matches == 26: return True

#             drop_index = ord(s2[l]) - ord('a')
#             if s2_count[drop_index] == s1_count[drop_index]:
#                 matches -= 1
#             s2_count[drop_index] -= 1
#             if s2_count[drop_index] == s1_count[drop_index]:
#                 matches += 1

#             add_index = ord(s2[r]) - ord('a')
#             if s2_count[add_index] == s1_count[add_index]:
#                 matches -= 1
#             s2_count[add_index] += 1
#             if s2_count[add_index] == s1_count[add_index]:
#                 matches += 1

#             l += 1

#         return matches == 26


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

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
            
            index_to_remove = ord(s2[l]) - ord('a')
            if s1_count[index_to_remove] == s2_count[index_to_remove]:
                match -= 1
            s2_count[index_to_remove] -= 1
            if s1_count[index_to_remove] == s2_count[index_to_remove]:
                match += 1

            index_to_add = ord(s2[r]) - ord('a')
            if s1_count[index_to_add] == s2_count[index_to_add]:
                match -= 1
            s2_count[index_to_add] += 1
            if s1_count[index_to_add] == s2_count[index_to_add]:
                match += 1
            
            l += 1
            r += 1
        
        return match == 26
            



         
        

        
        











































