# using min heap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x, y in points: # O(n)
            min_heap.append([(x**2 + y**2), x, y])
        
        heapq.heapify(min_heap) # O(n)

        res = []
        # O(klogn)
        for _ in range(k): # O(k)
            _, x, y = heapq.heappop(min_heap) # O(logn)
            res.append([x,y])
        
        return res
