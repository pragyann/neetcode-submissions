class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        k = max(piles)

        while l <= r:
            mid = (l + r) // 2
            rate = mid

            hours_required = 0 

            for pile in piles:
                hours_required += math.ceil(pile/rate)
            
            if hours_required <= h:
                r = mid - 1
                k = min(k, rate)
            else:
                l = mid + 1
        
        return k 
