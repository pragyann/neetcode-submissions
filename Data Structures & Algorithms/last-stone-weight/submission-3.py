class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1: # O(n)
            y, x = heapq.heappop(stones), heapq.heappop(stones) # O(logn)

            if x == y:
                continue
            
            heapq.heappush(stones, y-x)
        
        stones.append(0)
        return abs(stones[0])



        