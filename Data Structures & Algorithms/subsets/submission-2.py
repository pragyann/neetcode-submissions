class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums: # O(n)
            res += [subset + [num] for subset in res] # O(2^n)

        return res