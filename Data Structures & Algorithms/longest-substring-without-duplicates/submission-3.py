class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        # vocab = set()

        current_leng = 0
        for i, c in enumerate(s):
            j = i
            seq_len = 0
            vocab = set()

            while j < len(s) and s[j] not in vocab:
                seq_len += 1
                vocab.add(s[j])
                j += 1
            
            longest = max(longest, seq_len)
             
        
        return longest