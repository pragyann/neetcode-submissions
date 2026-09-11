class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1

        bucket = [[] for i in range(len(nums))]

        for n, freq in freq_map.items():
            bucket[freq-1].append(n)

        res = []
        for nums in bucket[::-1]:
            for n in nums:
                res.append(n)
                if len(res) == k:
                    return res
        