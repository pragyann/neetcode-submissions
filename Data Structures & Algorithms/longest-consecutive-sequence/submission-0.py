class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq_length = 0

        def is_start(n):
            return n-1 not in nums_set

        for num in nums:
            if not is_start(num):
                continue
            
            seq_length = 0
            next_in_seq = num
            while next_in_seq in nums_set:
                seq_length += 1
                next_in_seq = next_in_seq+1
            
            longest_seq_length = max(longest_seq_length, seq_length)
        
        return longest_seq_length