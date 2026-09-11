# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         triplets = []
        
#         nums.sort()

#         for i,target in enumerate(nums):
#             if i > 0 and target == nums[i-1]:
#                 continue

#             l, r = i+1, len(nums) - 1

#             while l < r:
#                 t_sum = nums[l] + nums[r] + target                   
                
#                 if t_sum > 0:
#                     r -= 1 
#                 elif t_sum < 0:
#                     l += 1
#                 else:
#                     triplets.append([nums[i], nums[l], nums[r]])
#                     l += 1
#                     while nums[l] == nums[l-1] and l < r:
#                         l += 1
                
#         return triplets





# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         triplets = []

#         nums.sort()

#         for i, target in enumerate(nums):
#             if i > 0 and target == nums[i - 1]:
#                 continue
            
#             l, r = i+1, len(nums) - 1

#             while l < r:
#                 three_sum = nums[i] + nums[l] + nums[r]

#                 if three_sum > 0:
#                     r-=1
#                 elif three_sum < 0:
#                     l+=1
#                 else:
#                     triplets.append([nums[i], nums[l], nums[r]])
#                     l+=1
#                     while nums[l] == nums[l-1] and l<r:
#                         l+=1
        
#         return triplets



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        i = 0
        while i < len(nums):
            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
        
        return triplets
            

































