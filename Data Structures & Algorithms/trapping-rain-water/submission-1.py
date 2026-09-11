# class Solution:
#     def trap(self, height: List[int]) -> int:
#         max_area = 0

#         left_max = [0] * len(height)
#         right_max = [0] * len(height)

#         for i in range(len(height)):
#             if i == 0:
#                 left_max[i] = height[i]
#                 continue
#             left_max[i] = max(left_max[i-1], height[i])

#         for i in range(len(height) - 1, -1, -1):
#             if i == len(height) - 1:
#                 right_max[i] = height[i]
#                 continue
#             right_max[i] = max(height[i], right_max[i+1])
        
#         for i in range(len(height)):
#             max_area += min(left_max[i], right_max[i]) - height[i]

#         return max_area

#         # Time complexity - O(n)
#         # Space complexity - O(n)

#         # This can be done with O(1) space complexity using two pointers.

class Solution:
    def trap(self, height: List[int]) -> int:
        max_area = 0

        l, r = 0, len(height) - 1

        left_max, right_max = height[l], height[r]

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                max_area += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                max_area += right_max - height[r]
        return max_area
        