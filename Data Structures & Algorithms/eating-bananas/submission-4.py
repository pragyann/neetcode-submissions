class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # max(piles) -> len(piles) hours

        min_k = max(piles)

        while l <= r:
            k = (l+r) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            
            print(k, hours)

            if hours <= h: # this means that k is valid and can finish within h, try to minimize k by looking on the left
                r = k - 1
                min_k = min(min_k, k)
            elif hours > h: # this means that it can't be finished within h, try to increase the speed of eating k
                l = k + 1
        
        return min_k



