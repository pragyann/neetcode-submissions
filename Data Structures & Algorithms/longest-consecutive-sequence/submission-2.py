# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums_set = set(nums)
#         longest_seq_length = 0

#         for num in nums:
#             if n-1 in nums_set:
#                 continue
            
#             seq_length = 0
#             next_in_seq = num
#             while next_in_seq in nums_set:
#                 seq_length += 1
#                 next_in_seq = next_in_seq+1
            
#             longest_seq_length = max(longest_seq_length, seq_length)
        
#         return longest_seq_length




class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest_seq = 0

        for n in nums:
            if n-1 in nums_set:
                continue
            
            l = 0
            next_seq_val = n
            while n in nums_set:
                l += 1
                n += 1
            
            longest_seq = max(longest_seq, l)

        return longest_seq






























