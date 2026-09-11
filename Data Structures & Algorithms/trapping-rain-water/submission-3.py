# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0
            
#         max_water = 0

#         l, r = 0, len(height) - 1

#         left_max, right_max = height[l], height[r]

#         while l < r:
#             if left_max < right_max:
#                 l += 1
#                 left_max = max(left_max, height[l])
#                 max_water += left_max - height[l]
#             else: 
#                 r -= 1
#                 right_max = max(right_max, height[r])
#                 max_water += right_max - height[r]

#         return max_water


        
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         max_water = 0

#         left_max = [0] * len(height)
#         right_max = [0] * len(height)

#         for i in range(1, len(height)):
#             left_max[i] = max(left_max[i-1], height[i-1])
        
#         for i in range(len(height) - 2, -1, -1):
#             right_max[i] = max(right_max[i+1], height[i+1])
        
#         for i, h in enumerate(height):
#             l = left_max[i]
#             r = right_max[i]

#             water = max(min(l, r) - h, 0)

#             max_water += water
        
#         return max_water
    
class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r] 

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                max_water += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                max_water += right_max - height[r]
        
        return max_water















































