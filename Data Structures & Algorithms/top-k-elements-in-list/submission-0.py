class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            freq = freq_map.get(num) if freq_map.get(num) != None else 0
            freq_map[num] = freq + 1;

        buckets = [[] for _ in range(len(nums))]

        for num in freq_map:
            bucket_index = freq_map[num] - 1
            buckets[bucket_index].append(num)

        flattened_bucket = []
        for bucket in buckets:
            flattened_bucket.extend(bucket)
        
        return flattened_bucket[-k:]
            
        