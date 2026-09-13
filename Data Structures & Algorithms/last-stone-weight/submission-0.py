class MaxHeap:
    def __init__(self, nums: List[int]):
        self.min_heap = [-n for n in nums]
        heapq.heapify(self.min_heap)
    
    def push(self, item: int):
        heapq.heappush(self.min_heap, -item)
    def pop(self) -> int:
        return -heapq.heappop(self.min_heap)
    def size(self) -> int:
        return len(self.min_heap)
        
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = MaxHeap(stones) # O(n)

        while max_heap.size() >= 2:
            y, x = max_heap.pop(), max_heap.pop()

            if x == y:
                continue
            
            max_heap.push(y-x)
        
        return max_heap.pop() if max_heap.size() else 0 



        