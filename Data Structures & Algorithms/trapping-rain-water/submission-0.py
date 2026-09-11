class Solution:
    def trap(self, height: List[int]) -> int:
        max_area = 0

        # l, r = 0, len(height) - 1

        # left_max, right_max = height[l], height[r]

        # while l < r:

        left_max = [0] * len(height)
        right_max = [0] * len(height)

        for i in range(len(height)):
            if i == 0:
                left_max[i] = height[i]
                continue
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                right_max[i] = height[i]
                continue
            right_max[i] = max(height[i], right_max[i+1])
        
        for i in range(len(height)):
            max_area += min(left_max[i], right_max[i]) - height[i]

        
        return max_area