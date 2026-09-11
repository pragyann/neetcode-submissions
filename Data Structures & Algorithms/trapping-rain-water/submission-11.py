class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0 

        left_max, right_max = [0] * len(height), [0] * len(height)

        for i in range(len(height)):
            if i == 0:
                left_max[i] = height[i]
                continue
            left_max[i] = max(height[i], left_max[i-1])
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                right_max[i] = height[i]
                continue
            right_max[i] = max(height[i], right_max[i+1])

        print(left_max)
        print(right_max)
        
        for i, h in enumerate(height):
            rect_height = min(left_max[i], right_max[i])
            print(rect_height, h)
            if rect_height <= h:
                continue
            
            res += (rect_height - h)
        
        return res

