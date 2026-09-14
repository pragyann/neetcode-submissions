class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            d = (x**2) + (y**2)
            heapq.heappush(heap, [-d, x, y])

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for _, x, y in heap:
            res.append([x,y])
        
        return res