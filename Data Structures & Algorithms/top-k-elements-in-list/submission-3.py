class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {} # {num: freq}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        bucket = []
        for _ in range(len(nums)):
            bucket.append([])
        
        for num, f in freq_map.items():
            bucket[f-1].append(num)
        
        res = []
        for items in bucket[::-1]:
            for item in items:
                res.append(item)
                if len(res) == k:
                    return res

        
