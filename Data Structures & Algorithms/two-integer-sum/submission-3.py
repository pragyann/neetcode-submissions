class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {} # {sum_needed_for_target: index}

        for index, num in enumerate(nums):
            diff = target-num

            if diff in diff_map:
                return [diff_map[diff], index]
            
            diff_map[num] = index
        
        return []

