class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {} # visited_number: postition

        for i, n in enumerate(nums):
            diff = target - n
            if diff in visited:
                return [visited[diff], i]
            
            visited[n] = i
        