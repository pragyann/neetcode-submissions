class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)
        
        buckets = [[] for i in range(len(nums) + 1)]

        for num, freq in freq_dict.items():
            buckets[freq].append(num)

        top_k = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k
            
        