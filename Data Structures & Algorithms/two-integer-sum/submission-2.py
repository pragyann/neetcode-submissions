class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {} # {number: index}

        for (i, n) in enumerate(nums):
            difference = target - n

            if diff_map.get(difference) != None:
                return [diff_map.get(difference), i]

            diff_map[n] = i   
        return []
