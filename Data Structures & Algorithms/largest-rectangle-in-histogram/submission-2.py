class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0 
        stack = [] # (index, height)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                popped_i, popped_h = stack.pop()
                max_area = max((i - popped_i) * popped_h, max_area)

                start = popped_i
            
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max((len(heights) - i) * h, max_area)
        
        return max_area


