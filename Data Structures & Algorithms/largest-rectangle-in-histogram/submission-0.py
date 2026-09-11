class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0 
        stack = [] # pair(index:height)

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                popped_i, popped_h = stack.pop()
                area = popped_h * (i - popped_i)
                max_area = max(max_area, area)
                start = popped_i
            
            stack.append((start, height))
        
        for i, height in stack:
            area = height * (len(heights) - i)
            max_area = max(max_area, area)
        
        return max_area