class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        # O(nlogk)
        for x, y in points: # O(n)
            d = (x**2 + y**2)
            heapq.heappush(max_heap, [-d, x, y]) # O(logk)

            if len(max_heap) > k:
                heapq.heappop(max_heap) # O(logk)
            
        res = []
        # O(klogk)
        while max_heap: # O(k)
            _, x, y = heapq.heappop(max_heap) # O(logk)
            res.append([x, y])
        
        return res