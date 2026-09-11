class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]

        while l < r:
            if left_max < right_max:
                l += 1
                res += max(left_max - height[l], 0)
                left_max = max(left_max, height[l])
            else:
                r -= 1
                res += max(right_max - height[r], 0)
                right_max = max(right_max, height[r])
        
        return res