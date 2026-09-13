class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.min_heap = k, nums
        heapq.heapify(self.min_heap) # O(n)

        # O(nlogn)
        while len(self.min_heap) > k: # O(n-k)
            heapq.heappop(self.min_heap) # O(logn)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]




