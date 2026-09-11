class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0 
        left_max, right_max = 0, 0
        l, r = 0, len(height) - 1

        while l <= r:
            if left_max < right_max:
                left_max = max(left_max, height[l])
                print(f"left_max={left_max}, added={left_max} - {height[l]}")
                res += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                print(f"right_max={right_max}, added={right_max} - {height[r]}")
                res += right_max - height[r]
                r -= 1
        
        return res
