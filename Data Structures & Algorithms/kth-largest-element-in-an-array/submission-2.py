class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums] # O(n)
        heapq.heapify(nums) # O(n)

        res = None
        for _ in range(k): # O(k)
            res = -heapq.heappop(nums) # O(logn)
        return res