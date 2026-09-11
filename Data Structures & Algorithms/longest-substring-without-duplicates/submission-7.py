# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         longest = 0

#         current_leng = 0
#         for i, c in enumerate(s):
#             j = i
#             seq_len = 0
#             vocab = set()

#             while j < len(s) and s[j] not in vocab:
#                 seq_len += 1
#                 vocab.add(s[j])
#                 j += 1
            
#             longest = max(longest, seq_len)
             
        
#         return longest




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 

        l = 0
        vocab = set()

        for r in range(len(s)):
            
            while s[r] in vocab:
                vocab.remove(s[l])
                l += 1
            
            vocab.add(s[r])

            res = max(res, r - l +1)
        
        return res

        